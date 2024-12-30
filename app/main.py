from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, annotations, predictions, admin

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(annotations.router, prefix="/annotations", tags=["annotations"])
