import yt_dlp

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from youtubesearchpython import VideosSearch

from ..YukkiUtilities.helpers.ytdl import ytdl_opts 
from ..YukkiUtilities.helpers.filters import command
from ..YukkiUtilities.helpers.thumbnails import down_thumb
from Yukki.YukkiUtilities.database.queue import remove_active_chat
from Yukki.YukkiUtilities.database.sudo import get_sudoers, remove_sudo
from ..YukkiUtilities.helpers.inline import start_keyboard, personal_markup
from Yukki import app, BOT_USERNAME, BOT_ID, ASSID, ASSNAME, ASSUSERNAME, OWNER, SUDOERS
from Yukki.YukkiUtilities.database.chats import get_served_chats, is_served_chat, add_served_chat


def start_pannel():  
    buttons = [
            [
                InlineKeyboardButton(text="📚 Commands", url="https://telegra.ph/Veez-Mega-Guide-01-10")
            ],
            [ 
                InlineKeyboardButton(text="📣 Channel", url="https://t.me/levinachannel"),
                InlineKeyboardButton(text="💭 Group", url="https://t.me/VeezSupportGroup")
            ],
    ]
    return "✨ This is veez mega, a bot that can play music trough the Telegram Group video chat feature.", buttons


pstart_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url="https://t.me/VeezMegaBot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "📚 Commands", url="https://telegra.ph/Veez-Mega-Guide-01-10"),
                    InlineKeyboardButton(
                        "❓ Setup Guide", url="https://telegra.ph/Veez-Mega-Guid-11-19")
                ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url="https://t.me/VeezSupportGroup"), 
                    InlineKeyboardButton(
                        "📎 Official Channel", url="https://t.me/levinachannel")
                ],
            ]
        )


welcome_captcha_group = 2



 
