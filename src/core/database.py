from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

# 1. Create the engine: This is the actual connection to the DB
engine = create_engine(settings.DATABASE_URL)

# 2. Create a SessionLocal: Each request to our API will get its own database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create the Base class: Our models will inherit from this to be recognized by SQLAlchemy
Base = declarative_base()

# Dependency to get a DB session for our routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()