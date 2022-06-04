import asyncio
from os import environ
from pyrogram import Client, filters, idle

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
LM = "<b>hey {},\n this type of messages not allowed in the group </b>"

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
@User.on_message(filters.new_chat_members & filters.chat(GROUPS))
async def auto_welcoime(user, message):
    chat=message.chat
    usr=message.from_user
    cg = await user.send_message(chat_id=chat.id, text=f"ʜɪ {usr.first_name} \n 💐 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {chat.title}")
    await asyncio.sleep(16) 
    await cg.delete()
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
