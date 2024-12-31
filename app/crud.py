from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_prediction(db: Session, prediction: schemas.PredictionCreate):
    db_prediction = models.Prediction(
        model_id=prediction.model_id,
        sample_id=str(prediction.sample_id),
        probabilities=str(prediction.probabilities)
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

def create_annotation(db: Session, annotation: schemas.AnnotationCreate):
    db_annotation = models.Annotation(
        user_id=annotation.user_id,
        prediction_id=annotation.prediction_id,
        feedback=str(annotation.feedback)
    )
    db.add(db_annotation)
    db.commit()
    db.refresh(db_annotation)
    return db_annotation
