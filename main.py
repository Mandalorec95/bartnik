
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import start, recommendation, feedback, favorites, history, stats

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Подключаем все роутеры
dp.include_routers(
    start.router,
    recommendation.router,
    feedback.router,
    favorites.router,
    history.router,
    stats.router
)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
