from epbot import *
from pyrogram import filters
from epbot import epic
from pyrogram import *
from pyrogram.types import *
from config import *
from epbot.fsub import *



import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from helper.decorators import humanbytes
from config import *
from database.db import Database
from asyncio import *
import heroku3
import requests
from database.check_user import *


#+_+_$($(_??_?_!!_!!$++$+$!+$++#+:@!_()_//_/_)_))_(_+#!@!;_+"(#!;1)_)_-#+



async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        
#------------------------------Db End---------------------------------------------------------#       

DATABASE_URL=MONGO_URL
db = Database(DATABASE_URL, "rmbgbot")


START_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🌐 ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ 🌐', url='https://telegram.me/EpicBotsSl')
        ],
        [
            InlineKeyboardButton('✨ ʜᴇʟᴘ ✨', callback_data='help'),
            InlineKeyboardButton('🍁 ᴀʙᴏᴜᴛ 🍁', callback_data='about')
        ],
        [
            InlineKeyboardButton('💫 ꜱᴜᴘᴘᴏʀᴛᴇʀ 💫', url='https://removebg.com')
        ]
    ]
)


@epic.on_message(filters.command("start"))
async def start(epic, message):
    if await forcesub(epic, message):
       return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        if -1001741009206:
            await apic.send_message(
                -1001741009206,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @RemBackBot !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.delete()
    await message.reply_photo("https://telegra.ph/file/27265e01c11225f2a0969.jpg", caption=f"""
ʜᴇʟʟᴏ ||{message.from_user.mention}||
**🍁ɪ ᴀᴍ ᴍᴇᴅɪᴀ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ ʙᴏᴛ**
__ɪ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ʙᴀᴄᴋɢʀᴏᴜɴᴅꜱ..
🍃 ᴠɪᴅᴇᴏ ᴀɴᴅ ᴘʜᴏᴛᴏꜱ__
🍂 ᴄʟɪᴄᴋ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴇʟᴘ
🍂 ᴄʟɪᴄᴋ ᴛᴏ ᴀʙᴏᴜᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʙᴏᴛ
ᴊᴜꜱᴛ ɴᴏᴡ ꜱᴇɴᴅ ᴍᴇ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ɪ ᴡɪʟʟ ꜱᴇɴᴅ ᴘʜᴏᴛᴏ
ᴡʜɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʙᴀʙʏ !""", reply_markup=START_BUTTON)


