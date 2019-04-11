import pathlib

from envparse import env
import yarl

try:
    env.read_envfile()
except:
    pass

DEBUG = env.bool("DEBUG")
BOT_API_TOKEN = env.str("BOT_API_TOKEN")

PATH = pathlib.Path(__file__).parents[1]
REDIS_URL = yarl.URL(env.str("REDIS"))
