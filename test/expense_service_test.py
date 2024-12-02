from datetime import datetime

from repository.expense_repository import ExpenseRepository
from schemas.enum.expense_category import ExpenseCategory
from service.expense_service import ExpenseService

expense_repository = ExpenseRepository("../repository/data.json")
expense_service = ExpenseService(expense_repository)

print("===== add test =====")
expense_service.add_expense(
    datetime.now(),
    "스타벅스",
    "아이스아메리카노",
    4_500,
    ExpenseCategory.DRINK
)

expense_service.add_expense(
    datetime.now(),
    "고향옥",
    "얼큰 순대국",
    10_000,
    ExpenseCategory.DRINK
)

print("===== get test =====")
print(expense_service.get_expenses())
