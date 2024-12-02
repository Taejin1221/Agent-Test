from datetime import datetime

from ai_model.gpt_model import GPTModel
from prompt.chat_prompt import GET_ACTION
from prompt.functions import FUNCTIONS

gpt_model = GPTModel()

message = input("명령하세요: ")
print(gpt_model.generate_action(GET_ACTION.format(curr_time=datetime.now()), FUNCTIONS, message))
