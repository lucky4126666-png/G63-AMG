from openai import OpenAI
import os
from memory import get

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(user_id, text):
    history = get(user_id)

    messages = [{"role": "user", "content": m} for m in history]
    messages.append({"role": "user", "content": text})

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return res.choices[0].message.content
