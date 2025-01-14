import base64
from sqlalchemy import Column, Integer, JSON, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False, default=0)  # Foreign key for the Model relationship
    prediction_id = Column(Integer, nullable=False)
    prediction = Column(JSON, nullable=False)
    
    def __init__(self, model_id=None, model_name=None, prediction_id=None, prediction=None, data=None):
        """Override constructor to call the set_data method if needed."""
        # Ensure base initialization happens to handle the model fields properly
        super().__init__()
        self.model_id = model_id
        self.model_name = model_name
        self.prediction_id = prediction_id
        if prediction is not None:
            self.prediction = prediction
        if data is not None:
            self.set_data(data)
    
    def set_data(self, data: any):
        """Serializes data into a JSON-compatible format."""
        if isinstance(data, bytes):  # For binary data like images or PDFs
            # Base64 encode binary data
            data = {"type": "binary", "content": base64.b64encode(data).decode('utf-8')}
        elif isinstance(data, str):  # For string data
            data = {"type": "text", "content": data}
        elif isinstance(data, list):  # For list data (list of strings or integers)
            data = {"type": "list", "content": data}
        self.data = data

    def get_data(self):
        """Deserializes the data back to its original type."""
        if self.data.get("type") == "binary":
            return base64.b64decode(self.data["content"].encode('utf-8'))
        elif self.data.get("type") == "list":
            return self.data["content"]
        return self.data.get("content")

    
    annotations = relationship("Annotation", back_populates="prediction")
    model = relationship("Model", back_populates="predictions")