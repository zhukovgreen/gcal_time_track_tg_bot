import logging

from aiogram.contrib.fsm_storage.redis import (
    RedisStorage2,
)
from aiogram import Bot, Dispatcher

from .settings import DEBUG, BOT_API_TOKEN, REDIS_URL


logging.basicConfig(
    level="DEBUG" if DEBUG else "INFO"
)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)
storage = RedisStorage2(
    REDIS_URL.host,
    REDIS_URL.port,
    db=int(REDIS_URL.path[1:]),
)
bot = Bot(token=BOT_API_TOKEN, parse_mode="markdown")
dp = Dispatcher(bot, storage=storage)
