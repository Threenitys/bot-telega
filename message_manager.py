from pyrogram import Client
from constants import PHOTO_PATH
from database import update_last_interaction

async def send_message(app, chat_id, text):
    try:
        await app.send_message(chat_id, text)
        logger.success(f"Message sent to {chat_id}: {text}")
    except Exception as e:
        logger.error(f"Error sending message to {chat_id}: {e}")

async def send_photo(app, chat_id, photo_path):
    try:
        await app.send_photo(chat_id, photo_path)
        logger.success(f"Photo sent to {chat_id}")
    except Exception as e:
        logger.error(f"Error sending photo to {chat_id}: {e}")

async def process_user_messages(app, chat_id):
    await send_message(app, chat_id, "Добрый день!")
    await asyncio.sleep(60 * 90)  # 90 minutes
    await send_message(app, chat_id, "Подготовила для вас материал")
    await send_photo(app, chat_id, PHOTO_PATH)
    await update_last_interaction(chat_id)
