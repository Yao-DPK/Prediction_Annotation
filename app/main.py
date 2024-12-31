from fastapi import FastAPI
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