from pydantic import BaseModel
from typing import Optional

class FeedbackBase(BaseModel):
    feedback: str
    user_id: int
    prediction_id: int

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackOut(FeedbackBase):
    id: int

    class Config:
        orm_mode = True
