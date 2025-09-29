from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.dependencies import get_db

router = APIRouter()

@router.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"message": "DB is working!"}
