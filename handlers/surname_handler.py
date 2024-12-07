from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Введіть прізвище:")
    return 0  # SURNAME

async def surname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["surname"] = update.message.text
    await update.message.reply_text("Введіть ім'я:")
    return 1  # NAME

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Операция отменена.")
    return -1  # END


