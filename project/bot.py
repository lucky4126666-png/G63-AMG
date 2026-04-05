import asyncio, requests, os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message()
async def handle(msg: types.Message):
    if msg.chat.type not in ["group", "supergroup"]:
        return

    text = msg.text or ""

    if "ai" not in text.lower():
        return

    loading = await msg.reply("⚡ Đang xử lý...")

    res = requests.post("http://localhost:8000/api/ai", json={"text": text})

    await bot.edit_message_text(
        chat_id=msg.chat.id,
        message_id=loading.message_id,
        text=res.json()["reply"]
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
