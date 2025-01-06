from pydantic import BaseModel
from typing import Any

class PredictionBase(BaseModel):
    model_name: str
    prediction_id: int
    prediction: Any
    

class PredictionCreate(PredictionBase):
    pass

class PredictionsCreate(PredictionBase):
    prediction_id: list[int]
    prediction: list[Any]
    

class PredictionOut(PredictionBase):
    id: int

    class Config:
        orm_mode = True
