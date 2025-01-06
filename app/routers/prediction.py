from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.prediction import PredictionCreate, PredictionOut, PredictionsCreate
from app.db.session import get_db
from app.models.prediction import Prediction

router = APIRouter()

@router.post("/", response_model=PredictionOut)
def create_prediction(prediction_in: PredictionCreate, db: Session = Depends(get_db)):
    prediction = Prediction(
        model_name = prediction_in.model_name,
        prediction_id =  prediction_in.prediction_id,
        prediction = prediction_in.prediction
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    
    return prediction

@router.post("/", response_model=PredictionOut)
def create_predictions(prediction_in: PredictionsCreate, db: Session = Depends(get_db)):
    for i in range(len(prediction_in.prediction_id)):
        prediction = Prediction(
        model_name = prediction_in.model_name,
        prediction_id =  prediction_in.prediction_id,
        prediction = prediction_in.prediction
    )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
    
    return prediction


@router.get("/{prediction_id}", response_model=PredictionOut)
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    
    return prediction
