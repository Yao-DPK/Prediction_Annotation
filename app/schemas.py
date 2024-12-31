from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UtilisateurBase(BaseModel):
    nom: str
    email: EmailStr

class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str

class UtilisateurRead(UtilisateurBase):
    id: int

    class Config:
        from_attributes = True

class AnnotationBase(BaseModel):
    retour: str

class AnnotationCreate(AnnotationBase):
    utilisateur_id: int
    prediction_id: int

class AnnotationRead(AnnotationBase):
    id: int

    class Config:
        from_attributes = True

class PredictionBase(BaseModel):
    output: str
    input: str

class PredictionCreate(PredictionBase):
    pass

class PredictionRead(PredictionBase):
    id: int

    class Config:
        from_attributes = True

class ModelBase(BaseModel):
    name: str

class ModelCreate(ModelBase):
    pass

class ModelRead(ModelBase):
    id: int

    class Config:
        from_attributes = True
