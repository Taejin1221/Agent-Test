import json
from datetime import datetime

from schemas.enum.income_category import IncomeCategory
from schemas.income import Income


class IncomeRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _read_data(self) -> dict:
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _write_data(self, data: dict) -> None:
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_income(
            self,
            date: datetime,
            source: str,
            amount: int,
            category: IncomeCategory,
            desc: str | None
    ):

        data = self._read_data()
        expense = {
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "source": source,
            "category": category.value,
            "amount": amount,
            "description": desc
        }
        data["incomes"].append(expense)
        data["balances"] += amount
        self._write_data(data)

    def get_incomes(self) -> list[Income]:
        data = self._read_data()
        expenses = data["incomes"]

        result = [Income(**expense) for expense in expenses]

        return result
