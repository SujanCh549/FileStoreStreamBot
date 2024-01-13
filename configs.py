import os
from os import getenv, environ


# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
	ON_HEROKU = True
	APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN','filestore-filmyhub.koyeb.app/') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'FileStoreStreamBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'FileStoreStreamBot'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
DISABLE_CHANNEL_BUTTON = bool(environ.get('DISABLE_CHANNEL_BUTTON', False))
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
STREAM_LOGS = environ.get('STREAM_LOGS','-1002082325170')
SESSION = environ.get('SESSION','MissRozy')
CUSTOM_CAPTION = environ.get('CUSTOM_CAPTION')

class Config(object):
  API_ID = int(os.environ.get("API_ID", "29692392"))
  API_HASH = os.environ.get("API_HASH", "948daec2dc8c979ceb0e4e5746cdd994")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6896166382:AAGHdyBDQrIh2-AWW2BxXBCiSVQ8KTAqFPs")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "TG_FileSharing_RoBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002082325170"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "vnshortener.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "6c5db31980885e46221e90106f1d47b8295aa0f8")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5123039648"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jeyesa3599:jeyesa3599@cluster0.aloblt2.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002114664669")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  LAZY_CHANNEL = int(os.environ.get('LAZY_CHANNEL', '-1002082325170'))
  LAZY_MODE = bool(os.environ.get("LAZY_MODE", "True"))
  LAZY_PIC = os.environ.get("LAZY_PIC","https://graph.org/file/8515052bfcd8461b7dcfd.jpg")
  LP_BTN_MAIN_CH_USRNM = os.environ.get("LP_BTN_MAIN_CH_USRNM")
  LP_CHANNEL_USRNM = os.environ.get("LP_CHANNEL_USRNM")
  LPCH_ADMIN_USRMN = os.environ.get("LPCH_ADMIN_USRMN")
  LP_CUSTOM_TEMPLATE= os.environ.get("LP_CUSTOM_TEMPLATE")
  # LP_CUSTOM_TEMPLATE= os.environ.get("LP_CUSTOM_TEMPLATE","{file_name} - example \n\n Please Upadate this template acording to you @LazyDeveloperr ")
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME', 20))
  ABOUT_BOT_TEXT = f"""
Tʜɪꜱ Iꜱ Aɴ Pᴇʀᴍᴀɴᴇɴᴛ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ. Sᴇɴᴅ Mᴇ Aɴʏ Vɪᴅᴇᴏ Oʀ Fɪʟᴇ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ A Sʜᴀʀᴇᴀʙʟᴇ Lɪɴᴋ.

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Tʜɪꜱ Pᴇʀꜱᴏɴ ](tg://settings)"""

  LAZY_HOME_TEXT = """
Hᴇʏ, [{}](tg://user?id={})\n\nI'ᴍ A Pᴇʀᴍᴀɴᴇɴᴛ **Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ**.

★ Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Pᴇʀᴍᴀɴᴇɴᴛ Sʜᴀʀᴇᴀʙʟᴇ Lɪɴᴋ.

«[⚡️𝗔𝘂𝘁𝗼 𝗠𝗼𝗱𝗲 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 ✅]»
 🥷 Nᴏᴡ Eᴠᴇʀʏᴛʜɪɴɢ Uᴘᴏɴ Mᴇ 🥷
"""
  HOME_TEXT = """
Hᴇʏ, [{}](tg://user?id={})\n\nI'ᴍ A Pᴇʀᴍᴀɴᴇɴᴛ **Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ**.

★ Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Pᴇʀᴍᴀɴᴇɴᴛ Sʜᴀʀᴇᴀʙʟᴇ Lɪɴᴋ.

«[⚡️𝗔𝘂𝘁𝗼 𝗠𝗼𝗱𝗲 𝗦𝘁𝗮𝘁𝘂𝘀 : 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 💢]»
 😏 Nᴏᴡ Eᴠᴇʀʏᴛʜɪɴɢ Uᴘᴏɴ Yᴏᴜ 😏
"""
