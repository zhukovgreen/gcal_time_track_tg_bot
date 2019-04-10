import logging

from aiohttp import web

from .bot import BotManager
from .settings import DEBUG


logging.basicConfig(
    level="DEBUG" if DEBUG else "INFO"
)
logger = logging.getLogger(__name__)


async def health_check(
    request: web.Request
) -> web.Response:
    return web.Response()


def run_bot():
    bot = BotManager()
    bot.start()
