from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://feedback_user:feedback_password@localhost:5433/feedback_db"

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
