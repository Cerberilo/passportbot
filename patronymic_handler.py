from telegram import Update
from telegram.ext import ContextTypes
from handlers.date_handler import show_calendar

async def patronymic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["patronymic"] = update.message.text

    await show_calendar(update, context)
    return 5  # CALENDAR


