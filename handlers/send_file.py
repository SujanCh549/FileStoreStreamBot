import asyncio
import requests
import string
import random
from configs import Config
from configs import *
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"Fɪʟᴇꜱ Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Aɴʏ Tɪᴍᴇ. Sᴏ Pʟᴇᴀꜱᴇ Fᴏʀᴡᴀʀᴅ Aɴʏ Wʜᴇʀᴇ Tᴏ Sᴀᴠᴇ Tʜᴇᴍ.\n\nHᴇʀᴇ Iꜱ Sʜᴀʀᴀʙʟᴇ Lɪɴᴋ Oꜰ Tʜɪꜱ Fɪʟᴇ:**\n"
            f"https://t.me/{Config.BOT_USERNAME}?start=PredatorHackerzZ_{str_to_b64(str(file_id))}",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)

        lazy_stream = f"{URL}watch/{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
                lazy_download = f"{URL}{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
                
                fileName = quote_plus(get_name(lazy_file))

                await lazy_file.reply_text(
                    text=f"•• Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇᴅ Fᴏʀ Iᴅ #{user_id} \n\n•• File Name : {fileName}",
                    quote=True,
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚀 Fᴀꜱᴛ Dᴏᴡɴʟᴏᴀᴅ", url=lazy_download),  # we download Link
                                                        InlineKeyboardButton('🖥️ Wᴀᴛᴄʜ Oɴʟɪɴᴇ', url=lazy_stream)]])  # web stream Link
                )
                return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id, 
                                          reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                  InlineKeyboardButton("🚀 Fᴀꜱᴛ Dᴏᴡɴʟᴏᴀᴅ", url=lazy_download),
                                                  InlineKeyboardButton("🖥️ Wᴀᴛᴄʜ Oɴʟɪɴᴇ", url=lazy_stream),
                                                ],
                                            ]),
                                             )
        
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)

    elif Config.FORWARD_AS_COPY is False:
            lazy_file = await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
            lazy_stream = f"{URL}watch/{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
            lazy_download = f"{URL}{str(lazy_file.id)}/{quote_plus(get_name(lazy_file))}?hash={get_hash(lazy_file)}"
            fileName = quote_plus(get_name(lazy_file))
            await lazy_file.reply_text(
                text=f"•• Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇᴅ Fᴏʀ Iᴅ #{user_id} \n\n•• File Name : {fileName}",
                quote=True,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚀 Fᴀꜱᴛ Dᴏᴡɴʟᴏᴀᴅ", url=lazy_download),  # we download Link
                                                    InlineKeyboardButton('🖥️ Wᴀᴛᴄʜ Oɴʟɪɴᴇ', url=lazy_stream)]])  # web stream Link
            )
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id,
                                              reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                  InlineKeyboardButton("🚀 Fᴀꜱᴛ Dᴏᴡɴʟᴏᴀᴅ", url=lazy_download),
                                                  InlineKeyboardButton("🖥️ Wᴀᴛᴄʜ Oɴʟɪɴᴇ", url=lazy_stream),
                                                ],
                                            ]),
                                             )

    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
        await message.delete()

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    asyncio.create_task(delete_after_delay(sent_message, 36000))

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()
