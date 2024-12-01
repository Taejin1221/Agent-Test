from datetime import datetime

from ai_model.gpt_model import GPTModel
from prompt.chat_prompt import INFERENCE_USER_INTENT, GET_ACTION, NORMAL_CONVERSATION
from prompt.functions import FUNCTIONS
from schemas.enum.expense_category import ExpenseCategory
from schemas.enum.income_category import IncomeCategory
from service.expense_service import ExpenseService
from service.income_service import IncomeService


class ChatService:
    def __init__(self, gpt_model: GPTModel, expense_service: ExpenseService, income_service: IncomeService):
        self.gpt_model = gpt_model
        self.expense_service = expense_service
        self.income_service = income_service

    def chat_with_agent(self, user_message: str) -> str:
        curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_intent = self.gpt_model.generate_response(INFERENCE_USER_INTENT, user_message)

        if user_intent == "normal_conversation":
            print("normal_conversation")
            return self.gpt_model.generate_response(NORMAL_CONVERSATION, user_message)
        elif user_intent == "command":
            print("command")
            command = self.gpt_model.generate_action(GET_ACTION.format(curr_time=curr_time), FUNCTIONS, user_message)

            func = command["function"]
            args = command["arguments"]
            if func == "add_expense":
                print(args["date"])
                self.expense_service.add_expense(
                    datetime.strptime(args["date"], "%Y-%m-%d %H:%M:%S"), args["place"], args["item"], args["amount"], ExpenseCategory(args["category"])
                )

                return f'요청이 성공적으로 처리되었습니다. {"-".join([args["date"], args["place"], args["item"], str(args["amount"]), args["category"]])}'
            elif func == "add_income":
                self.income_service.add_income(
                    datetime.strptime(args["date"], "%Y-%m-%d %H:%M:%S"), args["source"], args["amount"], IncomeCategory(args["category"])
                )
                return f'요청이 성공적으로 처리되었습니다. {"-".join([args["date"], args["source"], str(args["amount"]), args["category"]])}'
            elif func == "get_expenses":
                result = "소비 내역\n"
                for idx, expense in enumerate(self.expense_service.get_expenses()):
                    result += f"{idx}: {expense.date}-{expense.place}-{expense.item}-{expense.amount}원-{expense.category}\n"
                return result
            else:
                result = "수입 내역\n"
                for idx, income in enumerate(self.income_service.get_incomes()):
                    result += f"{idx}: {income.date}-{income.source}-{income.amount}원-{income.category}\n"
                return result
        else:
            return "처리할 수 없는 명령어입니다."
