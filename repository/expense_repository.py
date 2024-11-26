import json
from datetime import datetime

from schemas.enum.expense_category import ExpenseCategory
from schemas.expense import Expense


class ExpenseRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _read_data(self) -> dict:
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _write_data(self, data: dict) -> None:
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_expense(
            self,
            date: datetime,
            place: str,
            item: str,
            amount: int,
            category: ExpenseCategory,
            desc: str | None = None
    ):

        data = self._read_data()
        expense = {
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "place": place,
            "item": item,
            "category": category.value,
            "amount": amount,
            "description": desc
        }
        data["expenses"].append(expense)
        data["balances"] -= amount
        self._write_data(data)

    def get_expenses(self) -> list[Expense]:
        data = self._read_data()
        expenses = data["expenses"]

        result = [Expense(**expense) for expense in expenses]

        return result
