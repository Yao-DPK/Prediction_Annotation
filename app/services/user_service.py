from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password
from fastapi import HTTPException

def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def create_user(user: UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_current_user_info(user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    
    if user.name:
        db_user.name = user.name
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.hashed_password = hash_password(user.password)
    if user.is_admin is not None:
        db_user.is_admin = user.is_admin
    
    db.commit()
    db.refresh(db_user)
    return db_user

def update_any_user_info(user_id, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password:
        db_user.hashed_password = hash_password(user.password)
    if user.is_admin is not None:
        db_user.is_admin = user.is_admin
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_info(user_id: int, db: Session, current_user: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.email != current_user.get("email"):
        raise HTTPException(status_code=403, detail="Forbidden")
    
    db.delete(db_user)
    db.commit()
    return db_user

def verify_user_password(plain_password: str, hashed_password: str) -> bool:
    """Verify if the provided password matches the hashed password"""
    return verify_password(plain_password, hashed_password)
