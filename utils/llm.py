import openai
import os
from settings import OPENAI_API_KEY

class GPT4:
    def __init__(self, system_prompt):
        openai.api_key = OPENAI_API_KEY
        self.system_prompt = system_prompt
        self.conversation = [{"role": "system", "content": self.system_prompt}]
        self.model = "gpt-4"  # Replace this with the appropriate model when available

    def generate_response(self, user_query):
        self.conversation.append({"role": "user", "content": user_query})
        response = openai.ChatCompletion.create(
          model=self.model,
          messages=self.conversation,
        )
        self.conversation.append({"role": "assistant", "content": response.choices[0].message})
        return response.choices[0].message.content

    def add_query(self, user_query):
        response = self.generate_response(user_query)
        return response

    def get_history(self):
        return self.conversation