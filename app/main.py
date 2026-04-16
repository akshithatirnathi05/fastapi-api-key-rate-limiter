from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, protected

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(protected.router)

@app.get("/")
def read_root():
    return {"message": "API is working!"}