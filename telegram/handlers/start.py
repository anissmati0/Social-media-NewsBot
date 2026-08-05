from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    text = (f"Welcome {user.first_name}\n\n"
            "The available commands:\n"
            "Search for News: /findNews")
    
    await update.message.reply_text(text)
    