import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from AyiinRobot.events import register
from AyiinRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/21bca0a64032cd5b23b3c.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Yins Robot.** \n\n"
    TEXT += "♤ **I'm Working Properly** \n\n"
    TEXT += f"♤ **My Master : [Yins](https://t.me/AyiinXd)** \n\n"
    TEXT += f"♤ **Library Version :** `{telever}` \n\n"
    TEXT += f"♤ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"♤ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/YinzRobot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/AyiinXdSupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
