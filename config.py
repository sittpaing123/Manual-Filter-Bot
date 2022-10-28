
import os
import logging
from logging.handlers import RotatingFileHandler
from info import BOT_TOKEN, API_ID, API_HASH, DATABASE_URI, DATABASE_NAME2, AUTH_USERS, TG_USER_SESSION

# Get a bot token from botfather
TG_BOT_TOKEN = BOT_TOKEN

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = API_ID

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = API_HASH

# Generate a user session string 
TG_USER_SESSION = TG_USER_SESSION

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = DATABASE_URI 

# Your database name from mongoDB
DATABASE_NAME = DATABASE_NAME2

# ID of users that can use the bot commands
AUTH_USERS = AUTH_USERS

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "yes").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "yes").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
