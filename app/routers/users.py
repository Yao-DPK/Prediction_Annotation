from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.db.session import get_db
from app.services.user_service import create_user, get_user_by_email, update_any_user_info, update_current_user_info, delete_user_info
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

@router.put("/me", response_model=UserOut)
def update_user(user: UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_current_user_info(user, db, current_user)

@router.put("/{user_id}", response_model=UserOut)
def update_user_admin(user_id: int, user: UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    return update_any_user_info(user_id, user, db, current_user)

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    return delete_user_info(user_id, db, current_user)

@router.get("/protected-data", response_model=UserCreate)
def protected_data(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == current_user.email).first()
    return {"message": f"Welcome {user.name}, you have access!"}
