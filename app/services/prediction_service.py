from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.prediction import Prediction
from app.schemas.prediction import PredictionBase


def create_prediction(model_id: int, prediction_base: PredictionBase, db: Session):
    prediction = Prediction(
        model_id=model_id,
        prediction_id = prediction_base.prediction_id,
        prediction = prediction_base.prediction
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    
    return prediction

def get_prediction_by_data(prediction_base: PredictionBase, db: Session):
    return db.query(Prediction).filter(Prediction.id == prediction_base.prediction_id  and Prediction.prediction == prediction_base.prediction).first()