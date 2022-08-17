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
from epbot.module.rmbg import *
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




M_back = InlineKeyboardMarkup([[
                 InlineKeyboardButton('⏎', callback_data="mback")
                 ]])

HELP_TEXT = """--**More Help**--

- Just send me a photo or video
- I will download it
- I will send the photo or video without background
Made by @EpicBotsSl 🍁"""


ABOUT_TXT = f"""
👀ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝔫𝔞𝔳𝔞𝔫𝔧𝔞𝔫𝔞](https://t.me/NA_VA_N_JA_NA1)
🔥ᴄʜᴀɴɴᴇʟ : [ᴇᴘɪᴄ ᴅᴇᴠᴇꜱ](https://t.me/EpicBotsSl)
🔰ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
⚡ʙᴀꜱᴇᴅ ᴏɴ : [ᴘʏʀᴏɢʀᴀᴍ](https://pyrogram.org)
🚦ᴍᴀᴅᴇ ᴡɪᴛʜ : [ᴘʏᴛʜᴏɴ](https://python.org)

      [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ 🇱🇰](https://t.me/EpicBotsSl)
"""

START = f"""
ʜᴇʟʟᴏ ||{}||
**🍁ɪ ᴀᴍ ᴍᴇᴅɪᴀ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ ʙᴏᴛ**
__ɪ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ʙᴀᴄᴋɢʀᴏᴜɴᴅꜱ..
🍃 ᴠɪᴅᴇᴏ ᴀɴᴅ ᴘʜᴏᴛᴏꜱ__
🍂 ᴄʟɪᴄᴋ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴇʟᴘ
🍂 ᴄʟɪᴄᴋ ᴛᴏ ᴀʙᴏᴜᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʙᴏᴛ
ᴊᴜꜱᴛ ɴᴏᴡ ꜱᴇɴᴅ ᴍᴇ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ɪ ᴡɪʟʟ ꜱᴇɴᴅ ᴘʜᴏᴛᴏ
ᴡʜɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʙᴀʙʏ !"""


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


@epic.on_callback_query()  
async def tgm(epic, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "help":
         await update.message.edit_text(
             text=HELP_TEXT,
             reply_markup=M_back,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🕊️ Welcome to Help menu 🕊️ Join @EpicBotsSl",
         )
    elif update.data == "mback":
         await update.message.edit_text(
             text=START,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🕊️ Welcome back 🕊️ Join @EpicBotsSl",
         )
    elif update.data == "about":
         await update.message.edit_text(
             text=ABOUT_TXT,
             reply_markup=M_back,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🕊️ Welcome to about menu 🕊️ Join @EpicBotsSl",
         )
    elif update.data == "hp":
         await update.message.edit_text(
             text=HELP_TEXT,
             reply_markup=M_back,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🕊️ Welcome to Help menu 🕊️ Join @EpicBotsSl",
         )
    elif update.data == "close":
         await update.message.delete()

@epic.on_message(filters.command("stats")) 
async def startprivatsjwe(epic, message):
    countb = await db.total_users_count()
    countb = await db.total_users_count()
    count = await epic.get_chat_members_count(-1001620454933)
    counta = await epic.get_chat_members_count(-1001620454933)
    text=f"""
 ❍RmBg Bot Users ❍ : **{countb}**
 """
    await epic.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await epic.send_message(message.chat.id, text=text)

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]


@epic.on_message(filters.incoming & filters.chat(-1001609244993))
async def bchanl(epic, update, broadcast_ids={}): 
    all_users = await db.get_all_users()
    broadcast_msg= update
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break

    out = await epic.send_message(-1001741009206,f"Ads Broadcast Started! You will be notified with log file when all the users are notified.")
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
        
    async with aiofiles.open('broadcastlog.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
        
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    await asyncio.sleep(3)
    await out.delete()
    
    if failed == 0:
        await epic.send_message(-1001618730343, f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    else:
        await epic.send_document(-1001618730343, 'broadcastlog.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    os.remove('broadcastlog.txt')
