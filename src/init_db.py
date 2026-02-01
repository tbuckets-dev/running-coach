from src.core.database import engine, Base
# IMPORTANT: You must import your models here, otherwise SQLAlchemy 
# won't know they exist when it runs the "create_all" command.
from src.models.workout import User, Activity 

def init_db():
    print("Connecting to PostgreSQL at localhost:5433...")
    try:
        # metadata.create_all is a helper that creates tables if they don't exist
        Base.metadata.create_all(bind=engine)
        print("✅ Success! Your 'users' and 'activities' tables are ready.")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

if __name__ == "__main__":
    init_db()