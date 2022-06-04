import asyncio
import random
from os import environ
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple man to manage group </b>"
LM = "<b>{} this messages not allowed </b>"
MYRE = ["CAADBQAD2AMAAvjDaFSsTHfTpJDaShYE", "CAADBQADDQMAAtC6kVRSm-hyq9LjMRYE", "CAADBQADowEAAsuvXSk7LlkDJBYrnRYE", "CAADBQADAQcAAljMOFdOolwetNErQxYE", "CAADBQADeAMAArLJgFRXeMmuvdTQchYE", "CAADBQADsAMAAgYG8VSFaQgU6X596BYE", "CAADBQAD6AMAAi8MwVS1_PRa7JTUWxYE", "CAADBQADOgIAAnRfsFRgDjrWSQK3kxYE", "CAADBQADRAQAAlaVaVSKDdtGH1UJKhYE", ]

User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@User.on_message(filters.regex('Da') & filters.private)
async def start(user, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.regex('مژده') & filters.chat(GROUPS))
async def dfhhg(user, message):
    await Bot.delete_messages(message.chat.id, message.message_id)
@User.on_message(filters.regex('🔞') & filters.chat(GROUPS))
async def dfhhfg(user, message):
    await Bot.delete_messages(message.chat.id, message.message_id)
    cg = await message.reply(LM.format(message.from_user.first_name))
    await asyncio.sleep(5) 
    await cg.delete()
@User.on_message(filters.regex('about') & filters.private)
async def bot_info(user, message):
    buttons = [
        [
            InlineKeyboardButton("🎪 ɢʀᴏᴜᴘ  🎪", url="https://t.me/+eDjzTT2Ua6kwMTI1")
        ]
        ]
    a = await message.reply(text=f"🧞‍♂️ ɴᴀᴍᴇ : ᴀᴜᴛᴏ ғɪʟᴛᴇʀ v2.7 \n\n🎪 ᴄʀᴇᴀᴛᴏʀ : [sᴀʀᴀɴ](https://t.me/+aZIoNNlskWk4ODg1)\n\n📚 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3\n\n🌀 ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ 1.13.0\n\n🥀 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ᴍᴇ](https://t.me/nokiyirunnoippokitum)", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
    await asyncio.sleep(4) # program error 
    await a.delete()
    await user.send_sticker(chat_id=message.from_user.id, sticker=f"{random.choice(MYRE)}")
@User.on_message(filters.regex('a') & filters.private)
async def bot_srern(user, message):
    await user.send_sticker(chat_id=message.from_user.id, sticker=f"{random.choice(MYRE)}")

User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
