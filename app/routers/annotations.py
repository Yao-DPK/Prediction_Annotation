from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.AnnotationRead)
def create_annotation(annotation: schemas.AnnotationCreate, db: Session = Depends(get_db)):
    db_annotation = models.Annotation(**annotation.dict())
    db.add(db_annotation)
    db.commit()
    db.refresh(db_annotation)
    return db_annotation

@router.get("/{id}", response_model=schemas.AnnotationRead)
def get_annotation(id: int, db: Session = Depends(get_db)):
    annotation = db.query(models.Annotation).filter(models.Annotation.id == id).first()
    if not annotation:
        raise HTTPException(status_code=404, detail="Annotation not found")
    return annotation
