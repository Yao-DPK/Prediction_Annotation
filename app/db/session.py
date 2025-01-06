from datetime import time
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.base import Base
import time


# Create the engine to connect to PostgreSQL using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create tables in the database
    retries = 5
    for _ in range(retries):
        try:
            Base.metadata.create_all(bind=engine)  # Create tables
            inspector = inspect(engine)
            print(inspector.get_table_names())
            print("Database setup complete.")
            break  # Exit the loop if successful
        except Exception as e:
            print(f"Failed to create database tables: {e}. Retrying...")
            time.sleep(5)  # Retry after 5 seconds
            
            
# Dependency to get the current database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
