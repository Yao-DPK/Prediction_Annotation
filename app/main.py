import asyncio
from contextlib import asynccontextmanager, contextmanager
from fastapi import FastAPI
from app.db.session import init_db
from app.routers import auth, users, prediction, feedback, model

# Use lifespan context manager for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run the init_db function on app startup
    init_db()
    
    # Yield control to the application (start serving)
    yield
    
    # Add any cleanup code if needed during shutdown (optional)
    print("Shutting down the application.")
    

# Create the FastAPI app instance
app = FastAPI(lifespan=lifespan)



# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(prediction.router, prefix="/predictions", tags=["predictions"])
app.include_router(feedback.router, prefix="/feedbacks", tags=["feedbacks"])
app.include_router(model.router, prefix="/models", tags=["models"])

"""@app.on_event("startup")
def startup():
    # Run the init_db function on app startup
    init_db()"""
    
@app.get("/")
def root():
    return {"message": "Welcome to tg-org-backend!"}
