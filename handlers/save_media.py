import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

def generate_random_alphanumeric():
    """Generate a random 8-letter alphanumeric string."""
    characters = string.ascii_letters + string.digits
    random_chars = ''.join(random.choice(characters) for _ in range(8))
    return random_chars

def get_short(url):
    rget = requests.get(f"https://{Config.SHORTLINK_URL}/api?api={Config.SHORTLINK_API}&url={url}&alias={generate_random_alphanumeric()}")
    rjson = rget.json()
    if rjson["status"] == "success" or rget.status_code == 200:
        return rjson["shortenedUrl"]
    else:
        return url

    
async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=PredatorHackerzZ_{str_to_b64(str(SaveMessage.id))}"
        short_link = get_short(share_link)
        await editable.edit(
            f"**Batch Files Stored in my Database!**\n\nHere is the Permanent Link of your files: <code>{short_link}</code> \n\n"
            f"Just Click the link to get your files!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("♻️Original Link", url=share_link),
                  InlineKeyboardButton("🔗Short Link", url=short_link)]]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔗Short Link", url=short_link),
                                                InlineKeyboardButton("♻️Original Link", url=share_link)]])
        )

        if (Config.LAZY_MODE == True):

            thumbs= message.video.thumbs[0]
            file_id= thumbs.file_id
            lazy_channel = int(Config.LAZY_CHANNEL)
            location=await bot.download_media(file_id)
            lazypost_channel_username = (Config.LP_CHANNEL_USRNM)
            lazypost_ch_admin_usrnm = (Config.LPCH_ADMIN_USRMN)
            main_channel_username = (Config.LP_BTN_MAIN_CH_USRNM)
            main_btn_link = f"https://telegram.me/{main_channel_username}"
            file_name = message.caption
            caption_z = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            caption_za = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            caption_zab = f"{file_name}\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/LazyDeveloper'>⎝⎝✧ʟᴀᴢʏᴅᴇᴠᴇʟᴏᴘᴇʀ✧⎠⎠</a>"
            caption_zabi = f"{file_name}\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            lazy_dev = f"+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            lazypost_custom_template = f"{(Config.LP_CUSTOM_TEMPLATE)}\n\n{lazy_dev} ♥️"
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("★ Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ ★", url=share_link)],
                 [InlineKeyboardButton("⚡️✧ Gᴇᴛ Bᴀᴛᴄʜ Fɪʟᴇꜱ ✧⚡️", url=share_link)],
                ]
            )
            main_btn=InlineKeyboardMarkup(
                [[InlineKeyboardButton("★ Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ ★", url=share_link)],
                 [InlineKeyboardButton("⚡️✧ Gᴇᴛ Bᴀᴛᴄʜ Fɪʟᴇꜱ ✧⚡️", url=share_link)]
                ]
            )
            # ✧ Here is the condition for sending POST in movie channel
            if(Config.LP_CUSTOM_TEMPLATE):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=reply_markup)
            elif(Config.LP_CUSTOM_TEMPLATE and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=reply_markup)
            elif(Config.LP_CHANNEL_USRNM and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=reply_markup)
            elif(Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=main_btn)
            elif(Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=reply_markup)
            else:
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zabi,reply_markup=reply_markup)
                # ✧ Please don't add unnescesary things here >[LazyDeveloper]
                cptz = f"**Yᴏᴜʀ Fɪʟᴇ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Sᴛᴏʀᴇ**✅"
                k = await message.reply_text(text=cptz)
                await asyncio.sleep(30)
                await k.delete()
                
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            disable_web_page_preview=True)
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=PredatorHackerzZ_{str_to_b64(file_er_id)}"
        short_link = get_short(share_link)
        await editable.edit(
            "**Your File Stored in my Database!**\n\n"
            f"Here is the Permanent Link of your file: <code>{short_link}</code> \n\n"
            "Just Click the link to get your file!",
            reply_markup=InlineKeyboardMarkup(
               [[InlineKeyboardButton("♻️Original Link", url=share_link),
                  InlineKeyboardButton("🔗Short Link", url=short_link)]]
            ),
            disable_web_page_preview=True
        )

        if (Config.LAZY_MODE == True):
            thumbs= message.video.thumbs[0]
            file_id= thumbs.file_id
            lazy_channel = int(Config.LAZY_CHANNEL)
            location=await bot.download_media(file_id)
            lazypost_channel_username = (Config.LP_CHANNEL_USRNM)
            lazypost_ch_admin_usrnm = (Config.LPCH_ADMIN_USRMN)
            main_channel_username = (Config.LP_BTN_MAIN_CH_USRNM)
            main_btn_link = f"https://telegram.me/{main_channel_username}"
            file_name = message.caption
            caption_z = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            caption_za = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            caption_zab = f"{file_name}\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            caption_zabi = f"{file_name}\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            lazy_dev = f"+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/Sujan_BotZ'>✧ꜱᴜᴊᴀɴ_ʙᴏᴛꜱ✧</a>"
            lazypost_custom_template = f"{(Config.LP_CUSTOM_TEMPLATE)}\n\n{lazy_dev} ♥️"
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("★ Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ ★", url=share_link)]
                ]
            )
            main_btn=InlineKeyboardMarkup(
                [[InlineKeyboardButton("★ Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ ★", url=share_link)]
                ]
            )
            # ✧ Here is the condition for sending POST in movie channel ✧ LazyDeveloper ✧
            if(Config.LP_CUSTOM_TEMPLATE):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=reply_markup)
            elif(Config.LP_CUSTOM_TEMPLATE and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=reply_markup)
            elif(Config.LP_CHANNEL_USRNM and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=reply_markup)
            elif(Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=main_btn)
            elif(Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=reply_markup)
            else:
                # ✧ Please don't add unnescesary things here >[LazyDeveloper]
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zabi,reply_markup=reply_markup)
                cptz = f"**Yᴏᴜʀ Fɪʟᴇ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Sᴛᴏʀᴇ**✅"
                k = await message.reply_text(text=cptz)
                await asyncio.sleep(40)
                await k.delete()
                
    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
        
