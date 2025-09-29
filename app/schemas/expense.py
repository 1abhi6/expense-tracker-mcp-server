from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ExpenseBase(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = None
    category_id: Optional[int] = None
    date: Optional[datetime] = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseOut(ExpenseBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
