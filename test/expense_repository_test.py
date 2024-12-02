from datetime import datetime

from repository.expense_repository import ExpenseRepository
from schemas.enum.expense_category import ExpenseCategory

expenses_repository = ExpenseRepository("../repository/data.json")

print("===== add test =====")
expenses_repository.add_expense(
    datetime.now(),
    "스타벅스",
    "아이스아메리카노",
    4_500,
    ExpenseCategory.DRINK
)

expenses_repository.add_expense(
    datetime.now(),
    "고향옥",
    "얼큰 순대국",
    10_000,
    ExpenseCategory.DRINK
)

print("===== get test =====")
print(expenses_repository.get_expenses())
