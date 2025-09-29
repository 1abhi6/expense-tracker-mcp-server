from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.utils.dependencies import get_db, get_current_user

router = APIRouter()


@router.get("/expenses")
def list_expenses(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    return {"message": f"Expenses for user {current_user}"}
