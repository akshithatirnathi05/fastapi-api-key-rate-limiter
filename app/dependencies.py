from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.database import SessionLocal
from app import models

RATE_LIMIT = 5  # max requests
TIME_WINDOW = 60  # seconds

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(x_api_key: str = Header(...), db: Session = Depends(get_db)):
    api_key = db.query(models.APIKey).filter(models.APIKey.key == x_api_key).first()

    if not api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    now = datetime.utcnow()

    if api_key.last_request_time:
        if (now - api_key.last_request_time) < timedelta(seconds=TIME_WINDOW):
            if api_key.request_count >= RATE_LIMIT:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
            api_key.request_count += 1
        else:
            api_key.request_count = 1
    else:
        api_key.request_count = 1

    api_key.last_request_time = now
    db.commit()

    return api_key