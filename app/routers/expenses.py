from datetime import datetime
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.utils.dependencies import get_db, get_current_user
from app.models.expense import Expense

router = APIRouter()


# List all expenses for the current user
@router.get("/list-all")
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


# Create a new expense
@router.post("/create")
def create_expense(
    amount: float,
    description: str,
    category_id: int,
    date: str,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    """Create a new expense for the current user."""
    # Parse date string to date object
    try:
        # Try ISO format first
        parsed_date = datetime.fromisoformat(date).date()
    except ValueError:
        try:
            # Try DD/MM/YYYY format
            parsed_date = datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD or DD/MM/YYYY format")

    new_expense = Expense(
        amount=amount,
        description=description,
        category_id=category_id,
        date=parsed_date,
        user_id=current_user,
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return {
        "id": new_expense.id,
        "amount": new_expense.amount,
        "description": new_expense.description,
        "category_id": new_expense.category_id,
        "date": new_expense.date,
    }


