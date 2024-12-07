from telegram import Update
from telegram.ext import ContextTypes

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Введіть по-батькові:")
    return 2  # PATRONYMIC

