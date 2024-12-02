from datetime import datetime

from repository.income_repository import IncomeRepository
from schemas.enum.income_category import IncomeCategory

expenses_repository = IncomeRepository("repository/data.json")

print("===== add test =====")
expenses_repository.add_income(
    datetime.now(),
    "집",
    10000,
    IncomeCategory.ALLOWANCE,
    "와 용돈 받음~!~!"
)

expenses_repository.add_income(
    datetime.now(),
    "카카오테크 부트캠프",
    3_000_000,
    IncomeCategory.SALARY,
    "와 월급 받음~!~!"
)

print("===== get test =====")
print(expenses_repository.get_incomes())
