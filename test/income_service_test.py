from datetime import datetime

from repository.income_repository import IncomeRepository
from schemas.enum.income_category import IncomeCategory
from service.income_service import IncomeService

income_repository = IncomeRepository("repository/data.json")
income_service = IncomeService(income_repository)

print("===== add test =====")
income_service.add_income(
    datetime.now(),
    "집",
    10000,
    IncomeCategory.ALLOWANCE,
    "와 용돈 받음~!~!"
)

income_service.add_income(
    datetime.now(),
    "카카오테크 부트캠프",
    3_000_000,
    IncomeCategory.SALARY,
    "와 월급 받음~!~!"
)

print("===== get test =====")
print(income_service.get_incomes())
