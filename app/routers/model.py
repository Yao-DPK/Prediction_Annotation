from app.core.security import get_current_admin_user
from app.models.model import Model
from sqlalchemy.orm import Session
from app.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.model import ModelOut, ModelCreate
from app.services.model_service import get_model_by_name 



router = APIRouter()

@router.post("/", response_model=ModelOut)
def create_model(model_in: ModelCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    db_model = get_model_by_name(db, model_in.name)
    if db_model:
        raise HTTPException(status_code=400, detail="Model already registered")
    return create_model(model_in, db)
    
    