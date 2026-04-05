from openai import OpenAI
from core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(text):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}]
    )
    return res.choices[0].message.content
