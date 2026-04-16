from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    request_count = Column(Integer, default=0)
    last_request_time = Column(DateTime, nullable=True)