import json

from openai import OpenAI


class GPTModel:
    def __init__(self):
        self.client = OpenAI()

    def generate_response(self, prompt: str, user_message: str) -> str:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return response.choices[0].message.content

    def generate_action(self, prompt: str, tools: list[dict], user_message: str) -> dict:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )

        result = {
            "function": response.choices[0].message.tool_calls[0].function.name,
            "arguments": json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        }
        return result
