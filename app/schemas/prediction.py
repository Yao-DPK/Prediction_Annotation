from pydantic import BaseModel
from typing import Any

class PredictionBase(BaseModel):
    input_data: Any
    output_data: Any
    model_id: int

class PredictionCreate(PredictionBase):
    pass

class PredictionOut(PredictionBase):
    id: int

    class Config:
        orm_mode = True
