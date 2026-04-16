from fastapi import APIRouter, Depends
from app.dependencies import verify_api_key

router = APIRouter()

@router.get("/protected")
def protected_route(api_key=Depends(verify_api_key)):
    return {"message": "You accessed protected data!"}