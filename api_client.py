import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WEBAPP_URL = "https://chicken.valor-games.co/hack/chicken_index.php"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Abrir mini-app",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Si no te aparece el botón 'Abrir', pulsa el botón 'Abrir mini-app'",
        reply_markup=reply_markup,
    )

def main() -> None:
    application = Application.builder().token("8324004755:AAH47s9zHWXmLuP2W7DdSNRJLtCA3bqmbKo").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
