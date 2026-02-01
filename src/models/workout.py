from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from src.core.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    strava_id = Column(Integer, unique=True, index=True) # Their ID on Strava

class Activity(Base):
    __tablename__ = "activities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    strava_activity_id = Column(String, unique=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    
    # Data we get from Strava
    distance = Column(Float) # in meters
    moving_time = Column(Integer) # in seconds
    raw_data = Column(JSONB) # We store the whole JSON here just in case!