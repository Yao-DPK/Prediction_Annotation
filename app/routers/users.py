from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.db.session import get_db
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import Token, UserCreate, UserOut
from app.models.user import User
from app.db.session import get_db
from app.services.user_service import create_user, get_user_by_email, verify_user_password
from app.core.security import get_current_admin_user, get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    db_user = get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user, db)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, current_user: dict = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#update user
@router.put("/", response_model=UserOut)
def update_user(user: UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.email != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    if user.name:
        db_user.name = user.name
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.hashed_password = hash_password(user.password)
    if user.is_admin:
        db_user.role = user.is_admin
    
    db.commit()
    db.refresh(db_user)
    return db_user

#update user admin
@router.put("/{user_id}", response_model=UserOut)
def update_user_admin(user: UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    db_user = db.query(User).filter(User.id == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.email != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    if user.is_admin:
        db_user.is_admin = user.is_admin
    if user.password:
        db_user.hashed_password = hash_password(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user

#delete user
@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.email != current_user.email:
        raise HTTPException(status_code=403, detail="Forbidden")
    db.delete(db_user)
    db.commit()
    return db_user


@router.get("/protected-data", response_model=UserCreate)
def protected_data(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == current_user.email).first()
    return {"message": f"Welcome {user.name}, you have access!"}
