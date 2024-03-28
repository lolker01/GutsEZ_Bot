import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import telegram_bot_token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="i just want to be happy")
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="All i see every day is darkness")

if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_bot_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    start_handler = CommandHandler('name', name)
    application.add_handler(start_handler)

    start_handler = CommandHandler('weather', weather)
    application.add_handler(start_handler)



    application.run_polling()