from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from app.database import SessionLocal
from app import models
from app.schemas import APIKeyResponse  # ✅ NEW

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Generate API Key
@router.post("/generate-key", response_model=APIKeyResponse)  # ✅ UPDATED
def generate_api_key(db: Session = Depends(get_db)):
    new_key = str(uuid.uuid4())

    api_key = models.APIKey(key=new_key)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return {"api_key": new_key}