import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print("✅ API KEY LOADED:", os.getenv("OPENAI_API_KEY") is not None)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AIAgent:

    @staticmethod
    def summarize(text):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You summarize notes clearly and concisely."},
                {"role": "user", "content": text}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()

    @staticmethod
    def suggest_tasks(text):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Convert this note into actionable tasks."},
                {"role": "user", "content": text}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
