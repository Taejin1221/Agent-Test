from datetime import datetime

from pydantic import BaseModel

from schemas.enum.income_category import IncomeCategory


class Income(BaseModel):
    date: datetime
    source: str
    category: IncomeCategory
    amount: int
    description: str | None
