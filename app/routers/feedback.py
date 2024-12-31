from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.feedback import FeedbackCreate, FeedbackOut
from app.db.session import get_db
from app.models.annotation import Annotation

router = APIRouter()

@router.post("/", response_model=FeedbackOut)
def create_feedback(feedback_in: FeedbackCreate, db: Session = Depends(get_db)):
    feedback = Annotation(
        feedback=feedback_in.feedback,
        user_id=feedback_in.user_id,
        prediction_id=feedback_in.prediction_id,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    
    return feedback

@router.get("/{feedback_id}", response_model=FeedbackOut)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = db.query(Annotation).filter(Annotation.id == feedback_id).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    return feedback
