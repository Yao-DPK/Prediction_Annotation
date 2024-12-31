from fastapi import FastAPI
<<<<<<< HEAD
from app.routers import auth, users, prediction, feedback

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(prediction.router, prefix="/predictions", tags=["predictions"])
app.include_router(feedback.router, prefix="/feedbacks", tags=["feedbacks"])

@app.get("/")
def root():
    return {"message": "Welcome to tg-org-backend!"}
=======
from app.database import engine, Base
from app.routers import auth, annotations, predictions, admin

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(annotations.router, prefix="/annotations", tags=["annotations"])
>>>>>>> origin/main
