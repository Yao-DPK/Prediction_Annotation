from sqlalchemy import Column, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(JSON, nullable=False)   # JSON for flexibility
    output_data = Column(JSON, nullable=False)  # JSON for model's outputs

    annotations = relationship("Annotation", back_populates="prediction")
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False)
