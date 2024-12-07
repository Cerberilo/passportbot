import calendar
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_calendar(year, month):
    keyboard = []

    keyboard.append(
        [
            InlineKeyboardButton(f"{calendar.month_name[month]} {year}", callback_data=f"YEAR-{year}")
        ]
    )

    keyboard.append(
        [
            InlineKeyboardButton(day, callback_data="IGNORE")
            for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        ]
    )

    month_calendar = calendar.monthcalendar(year, month)
    for week in month_calendar:
        row = []
        for day in week:
            if day == 0:
                row.append(InlineKeyboardButton(" ", callback_data="IGNORE"))
            else:
                row.append(InlineKeyboardButton(str(day), callback_data=f"{year}-{month}-{day}"))
        keyboard.append(row)

    keyboard.append(
        [
            InlineKeyboardButton("<", callback_data=f"PREV-{year}-{month}"),
            InlineKeyboardButton(">", callback_data=f"NEXT-{year}-{month}"),
        ]
    )

    return InlineKeyboardMarkup(keyboard)

def create_year_selector(start_year, end_year):
    keyboard = []
    for year in range(start_year, end_year + 1):
        keyboard.append([InlineKeyboardButton(str(year), callback_data=f"SET-YEAR-{year}")])

    return InlineKeyboardMarkup(keyboard)

