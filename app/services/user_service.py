from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password

def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def create_user(user: UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_user_password(plain_password: str, hashed_password: str) -> bool:
    """Verify if the provided password matches the hashed password"""
    return verify_password(plain_password, hashed_password)  