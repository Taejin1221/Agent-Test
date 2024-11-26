from datetime import datetime

from pydantic import BaseModel

from schemas.enum.expense_category import ExpenseCategory


class Expense(BaseModel):
    date: datetime
    place: str
    item: str
    category: ExpenseCategory
    amount: int
    description: str | None
