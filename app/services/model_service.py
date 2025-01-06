from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.model import Model
from app.schemas.model import ModelCreate


def get_model_by_name(name: str, db: Session):
    return db.query(Model).filter(Model.name == name).first()

def check_model_exists(name: str, db: Session):
    return get_model_by_name(name, db) is not None

def create_model(model_in: ModelCreate, db: Session = Depends(get_db)):
    
    model = Model(
        name = model_in.name
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    
    return model