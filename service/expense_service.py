from datetime import datetime

from repository.expense_repository import ExpenseRepository
from schemas.enum.expense_category import ExpenseCategory
from schemas.expense import Expense


class ExpenseService:
    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository

    def add_expense(
            self,
            date: datetime,
            place: str,
            item: str,
            amount: int,
            category: ExpenseCategory,
            desc: str | None = None
    ):

        self.expense_repository.add_expense(date, place, item, amount, category, desc)

    def get_expenses(self) -> list[Expense]:
        return self.expense_repository.get_expenses()
