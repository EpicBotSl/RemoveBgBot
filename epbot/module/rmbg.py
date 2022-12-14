import os
import requests
from dotenv import load_dotenv
from pyrogram import filters
from epbot import epic
from epbot import *
from config import *
from pyrogram import *
from asyncio import *
from pyrogram.types import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ERROR_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='hp'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )


def removebg_video(file):
    return requests.post(
        "https://api.unscreen.com/v1.0/videos",
        files={"video_file": open(file, "rb")},
        headers={"X-Api-Key": UNSCREEN_API}
    )


#-----------------------------------------------------------------------#
#------------------------------uu------------------------------------------#ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ <s/ʟ>#
@epic.on_message(filters.private & (filters.photo | filters.video | filters.document))
async def remove_background(epic, update):
    if not (REMOVEBG_API):
        await update.reply_text(
            text="Error :- API not found",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    try:
        new_file_name = f"./{str(update.from_user.id)}"
        if (
            update.photo or (
                update.document and "image" in update.document.mime_type
            )
        ):
            new_file_name += ".png"
            file = await update.download()
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_image(file)
        elif (
            update.video or (
                update.document and "video" in update.document.mime_type
            )
        ):
            new_file_name += ".webm"
            file = await update.download()
            await message.edit_text(
                text="Video downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_video(file)
        else:
            await message.edit_text(
                text="Media not supported",
                disable_web_page_preview=True,
                reply_markup=ERROR_BUTTONS
            )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True
        )
    try:
        with open(new_file_name, "wb") as file:
            file.write(new_document.content)
    except Exception as error:
        await message.edit_text(
           text=error,
           reply_markup=ERROR_BUTTONS
        )
        return
    try:
        await update.reply_document(
            document=new_file_name,
            quote=True
        )
        try:
            os.remove(new_file_name)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=f"Error:- `{error}`",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


