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

    def generate_action(self, prompt: str, tools: list[dict], user_message: str) -> list[dict]:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )

        result = []
        for tool in response.choices[0].message.tool_calls:
            result.append({
                "function": tool.function.name,
                "arguments": json.loads(tool.function.arguments)
            })

        return result
