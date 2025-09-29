from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ExpenseBase(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = None
    category_id: Optional[int] = None
    date: Optional[str] = Field(
        description="Date must be in YYYY-MM-DD or DD/MM/YYYY format"
    )


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseOut(ExpenseBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
