from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Annotation(Base):
    __tablename__ = "annotations"

    id = Column(Integer, primary_key=True, index=True)
    feedback = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)

    user = relationship("User", back_populates="annotations")
    prediction = relationship("Prediction", back_populates="annotations")
