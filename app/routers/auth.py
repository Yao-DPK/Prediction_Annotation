from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import Token, UserLogin
from app.db.session import get_db
from app.models.user import User
from app.core.security import verify_password, create_access_token
from app.core.config import settings
from datetime import timedelta

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_user(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user =  db.query(User).filter(User.email == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # Verify password (assumes hashed_password and password matching check)
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    # Generate JWT token with user info (e.g., email, role)
    access_token = create_access_token(data={"sub": db_user.email, "is_admin": db_user.is_admin})
    return {"access_token": access_token, "token_type": "bearer"}