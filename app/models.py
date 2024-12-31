from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mot_de_passe = Column(String, nullable=False)

    annotations = relationship("Annotation", back_populates="utilisateur")

class Administrateur(Utilisateur):
    __tablename__ = "administrateurs"

    id = Column(Integer, ForeignKey("utilisateurs.id"), primary_key=True)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    output = Column(String, nullable=False)  # JSON stored as a string
    input = Column(String, nullable=False)

    annotations = relationship("Annotation", back_populates="prediction")

class Annotation(Base):
    __tablename__ = "annotations"

    id = Column(Integer, primary_key=True, index=True)
    retour = Column(String, nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    prediction_id = Column(Integer, ForeignKey("predictions.id"))

    utilisateur = relationship("Utilisateur", back_populates="annotations")
    prediction = relationship("Prediction", back_populates="annotations")

class Model(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    predictions = relationship("Prediction", back_populates="model")
