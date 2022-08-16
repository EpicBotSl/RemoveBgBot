import os
from dotenv import load_dotenv
from requests import get


load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
UNSCREEN_API = os.getenv("UNSCREEN_API", "JuASCiT65NFrcdTcBJbF2z6x").strip()
REMOVEBG_API = os.getenv("REMOVEBG_API", "8jgjzSPMVqWqKg45KvriAAv7").strip()

#UNSCREEN_API = JuASCiT65NFrcdTcBJbF2z6x
#REMOVEBG_API = 8jgjzSPMVqWqKg45KvriAAv7
