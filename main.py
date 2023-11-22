import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from pyrogram import Client, filters
from loguru import logger
from config import API_ID, API_HASH, BOT_TOKEN
from message_manager import process_user_messages
from database import check_user_in_database, register_user, update_last_interaction

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private)
async def handle_messages(_, message):
    chat_id = message.chat.id
    user_exists = await check_user_in_database(chat_id)

    if not user_exists:
        await register_user(chat_id)

    await update_last_interaction(chat_id)
    await process_user_messages(chat_id)

if __name__ == '__main__':
    app.run()
