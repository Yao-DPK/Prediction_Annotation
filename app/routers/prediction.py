from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_admin_user, get_current_user
from app.services.model_service import create_model
from sqlalchemy.orm import Session
from app.schemas.model import ModelCreate
from app.schemas.prediction import PredictionBase, PredictionCreate, PredictionIn, PredictionOut, PredictionsCreate
from app.db.session import get_db
from app.models.prediction import Prediction
from app.services.model_service import check_model_exists, get_model_by_name
from app.services.prediction_service import create_prediction, get_prediction_by_data

router = APIRouter()

@router.post("/", response_model=PredictionOut)
def register_prediction(prediction_in: PredictionIn, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    model = get_model_by_name(prediction_in.model_name, db)
    # Check if the model exists; if not, create it.
    if not model:
        model = create_model(ModelCreate(name = prediction_in.model_name), db)
    
    
    db_prediction = get_prediction_by_data(PredictionBase(prediction_id=prediction_in.prediction_id, prediction=prediction_in.prediction), db)
    if db_prediction:
        raise HTTPException(status_code=400, detail="Prediction already registered")
    return create_prediction(model.id, PredictionBase(prediction_id=prediction_in.prediction_id, prediction=prediction_in.prediction), db)

@router.post("/multi-create", response_model=PredictionOut)
def create_predictions(prediction_in: PredictionsCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    model = get_model_by_name(prediction_in.model_name, db)
    # Check if the model exists; if not, create it.
    if not model:
        model = create_model(ModelCreate(name = prediction_in.model_name), db)
        
    for i in range(len(prediction_in.prediction_id)):
        prediction = Prediction(
        model_id=model.id,
        prediction_id =  prediction_in.prediction_id[i],
        prediction = prediction_in.prediction[i]
    )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
    
    return prediction


@router.get("/{prediction_id}", response_model=PredictionOut)
def get_prediction(prediction_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    
    return prediction
