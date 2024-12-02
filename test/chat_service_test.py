from ai_model.gpt_model import GPTModel
from repository.balance_repository import BalanceRepository
from repository.expense_repository import ExpenseRepository
from repository.income_repository import IncomeRepository
from service.balance_service import BalanceService
from service.chat_service import ChatService
from service.expense_service import ExpenseService
from service.income_service import IncomeService

expense_service = ExpenseService(ExpenseRepository("repository/data.json"))
income_service = IncomeService(IncomeRepository("repository/data.json"))
balance_service = BalanceService(BalanceRepository("repository/data.json"))

gpt_model = GPTModel()
chat_service = ChatService(gpt_model, expense_service, income_service, balance_service)

while True:
    user_message = input("명령하세요: ")
    print(chat_service.chat_with_agent(user_message), end="\n\n")
