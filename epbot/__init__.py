from pyrogram import Client
from os import environ,sys,mkdir,path
import logging
from sys import executable
from Python_ARQ import ARQ
from aiohttp import ClientSession
from dotenv import load_dotenv
load_dotenv("config.env")
from config import *


from telethon import TelegramClient

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

try:
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)

#&---&-----&------&----++++-++++&--_&--+_+$+

#&-----&----&-----&---&------------&----------

AUTH_CHATS = "-1001741009206"

try:
    ARQ_API_KEY = "JRBVAR-JICHKN-DFLDNX-NPRGCH-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    aiohttpsession = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

except Exception as e:
    pass
    print(f"python arq key is not a valid string skiping it ...! Reason:{e}")
    aiohttpsession = ClientSession()
    arq = None


class epic(Client):
    def  __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"epbot/module"),
            workdir="./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30
        )
    async def start(self):
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists('/tmp/thumbnails/'):
            mkdir('/tmp/thumbnails/')
        LOGGER.info(f"Bot Started As @RemBackBot\n")
    
    async def stop(self,*args):
        await super().stop()
        LOGGER.info("Bot Stopped, Bye.")


#################################################
   ##.  #
   # #. #
   #. # #
   #.  ##
##########

TOKEN = "BOT_TOKEN"
NAME = TOKEN.split(":")[0]

tbot = TelegramClient(
    NAME, get_int_key("APP_ID", required=True), get_str_key("APP_HASH", required=True)
)

# Telethon
tbot.start(bot_token=TOKEN)
