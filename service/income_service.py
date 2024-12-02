from datetime import datetime

from repository.income_repository import IncomeRepository
from schemas.enum.income_category import IncomeCategory
from schemas.income import Income


class IncomeService:
    def __init__(self, income_repository: IncomeRepository):
        self.income_repository = income_repository

    def add_income(
            self,
            date: datetime,
            source: str,
            amount: int,
            category: IncomeCategory,
            desc: str | None = None
    ):

        self.income_repository.add_income(date, source, amount, category, desc)

    def get_incomes(self) -> list[Income]:
        return self.income_repository.get_incomes()
