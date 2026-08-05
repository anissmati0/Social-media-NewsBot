from telegram.ext import ApplicationBuilder, CommandHandler,CallbackQueryHandler
from handlers.start import start
from handlers.findnews import *
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("findnews", findnews))
    app.add_handler(
        CallbackQueryHandler(findnews_callback, pattern=f"^{CALLBACK_FIND_PREFIX}")
    )
    app.add_handler(
            CallbackQueryHandler(handle_create_post, pattern=f"^create:")
        )
    

    print("Bot is running. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()