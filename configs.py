# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "29692392"))
  API_HASH = os.environ.get("API_HASH", "948daec2dc8c979ceb0e4e5746cdd994")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6475207531:AAHIbTLcdTZ-6wC-bideI7I5KA3BxeY-G74")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Ullu_Desi_Porn_Adult_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001947421238"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "vnshortener.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "6c5db31980885e46221e90106f1d47b8295aa0f8")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5123039648"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jeyesa3599:jeyesa3599@cluster0.aloblt2.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002121361317")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001947421238")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Adult FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [Adult Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [@Sujan_BotZ](https://t.me/Sujan_BotZ)"""
  
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Adult FileStore Bot.

Join: @Sujan_BotZ"""
