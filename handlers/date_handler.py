import calendar
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.calendar_utils import create_calendar, create_year_selector
from handlers.gender_handler import send_gender_choice

async def show_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now()
    keyboard = create_calendar(now.year, now.month)
    await update.message.reply_text("Виберіть День Народження:", reply_markup=keyboard)

async def calendar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    data = query.data
    if data.startswith("PREV") or data.startswith("NEXT"):
        action, year, month = data.split("-")
        year = int(year)
        month = int(month)

        if action == "PREV":
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        elif action == "NEXT":
            month += 1
            if month == 13:
                month = 1
                year += 1

        keyboard = create_calendar(year, month)
        await query.edit_message_reply_markup(reply_markup=keyboard)
        return 5  # CALENDAR

    elif data.startswith("YEAR"):
        year = int(data.split("-")[1])
        keyboard = create_year_selector(year - 100, year + 1)
        await query.edit_message_reply_markup(reply_markup=keyboard)
        return 5  # CALENDAR

    elif data.startswith("SET-YEAR"):
        year = int(data.split("-")[2])
        month = datetime.datetime.now().month
        keyboard = create_calendar(year, month)
        await query.edit_message_reply_markup(reply_markup=keyboard)
        return 5  # CALENDAR

    elif data != "IGNORE":
        year, month, day = data.split("-")
        formatted_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        context.user_data["birthday"] = formatted_date
        
        await send_gender_choice(update, context)  # Сначала отправляем сообщение с выбором пола
        return 3  # GENDER

    return 5  # CALENDAR




        
