from pydantic import BaseModel

class ModelBase(BaseModel):
    name: str

class ModelCreate(ModelBase):
    pass

class ModelOut(ModelBase):
    id: int

    class Config:
        orm_mode = True
