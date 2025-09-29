from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.utils.dependencies import get_db, get_current_user
from app.models.expense import Expense

router = APIRouter()


@router.get("/expenses")
def list_expenses(
    db: Session = Depends(get_db), current_user: int = Depends(get_current_user)
):
    """Retrieve a list of all expenses for the current user."""
    expenses = db.query(Expense).filter(Expense.user_id == current_user).all()
    return [
        {
            "id": expense.id,
            "amount": expense.amount,
            "description": expense.description,
            "category_id": expense.category_id,
            "date": expense.date,
        }
        for expense in expenses
    ]
