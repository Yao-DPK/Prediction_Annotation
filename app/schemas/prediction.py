from pydantic import BaseModel
from typing import Any

class PredictionBase(BaseModel):
    prediction_id: int
    prediction: Any
    

class PredictionCreate(PredictionBase):
    model_id: int

class PredictionIn(PredictionBase):
    model_name: str


class PredictionsCreate(PredictionBase):
    model_name: str
    prediction_id: list[int]
    prediction: list[Any]
    

class PredictionOut(PredictionBase):
    id: int

    class Config:
        orm_mode = True
        
class PredictionsOut(PredictionBase):
    id: int

    class Config:
        orm_mode = True
