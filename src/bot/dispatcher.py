# src/bot/dispatcher.py
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from src.config import settings

# 1. Initialize Bot with HTML parsing as default (great for styling quotes!)
bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# 2. Initialize Dispatcher (The brain that processes incoming webhook updates)
dp = Dispatcher()