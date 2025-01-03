from sqlalchemy import inspect
from app.db.base import Base
from app.db.session import engine
from app.models.user import User 
from app.models.model import Model
from app.models.prediction import Prediction
from app.models.annotation import Annotation


def setup_database():
    """
    Create all database tables defined in the SQLAlchemy models.
    """
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    print(inspector.get_table_names()) 
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
