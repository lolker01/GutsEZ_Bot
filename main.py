import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, i am Guts_bot! How can i help you?')
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    last_name = update.effective_user.last_name

    message = update.message.text.lower()

    if "привіт" in message:

        if last_name is None:
            await update.message.reply_text(f'Привіт {update.effective_user.first_name}')

        else:
            await update.message.reply_text(f'Привіт {update.effective_user.first_name} {update.effective_user.last_name}')

    elif "допобачення" in message:

        if last_name is None:
            await update.message.reply_text(f'Бувай {update.effective_user.first_name}')

        else:
            await update.message.reply_text(f'Привіт {update.effective_user.first_name} {update.effective_user.last_name}')

    else:

        if last_name is None:
            await update.message.reply_text(f'{update.effective_user.first_name}, Шо ти висрав?')

        else:
            await update.message.reply_text(f'{update.effective_user.first_name} {update.effective_user.last_name}, Шо ти висрав?')


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()