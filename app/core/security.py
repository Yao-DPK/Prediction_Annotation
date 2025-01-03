from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Annotated, Union
from pydantic import BaseModel
from requests import Session
from app.models.user import User
from app.schemas.user import Token, TokenData
from app.db.session import get_db
from app.core.config import settings
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash passwords
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Function to create JWT token
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# Dependency to extract current user from JWT token
def get_current_user(token: Annotated[str,  Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        is_admin: str = payload.get("is_admin")
        if email is None or is_admin is None:
            raise credentials_exception
        
        token_data = TokenData(email=email, is_admin=is_admin)
        return token_data
    except JWTError:
        return None
    
    

# Dependency to check if user is an admin
def get_current_admin_user(current_user: dict = Depends(get_current_user)):
    if current_user.is_admin != True:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to perform this action")
    return current_user




