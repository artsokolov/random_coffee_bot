import os

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, ApplicationBuilder

from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ok, we got you...')


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler('start', start))

app.run_polling()
