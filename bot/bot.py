import asyncio, requests
from aiogram import Bot, Dispatcher, types
from core.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle(msg: types.Message):
    if msg.chat.type not in ["group", "supergroup"]:
        return

    text = msg.text or ""

    if "ai" not in text.lower():
        return

    await msg.reply("⚡ Đang xử lý...")

    res = requests.post("http://localhost:8000/ai", json={
        "user_id": msg.from_user.id,
        "text": text
    })

    job_id = res.json()["job_id"]

    await msg.reply(f"✅ Job: {job_id}")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
