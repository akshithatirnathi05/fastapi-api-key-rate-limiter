from pydantic import BaseModel

class APIKeyResponse(BaseModel):
    api_key: str