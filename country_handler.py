from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from handlers import surname_handler

# Не забудьте импортировать переменные, которые нужны в коде
from bot import COUNTRY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # Предлагаем пользователю выбрать страну
    keyboard = [
        [InlineKeyboardButton("Украина", callback_data="Ukraine")],
        [InlineKeyboardButton("Польша", callback_data="Poland")],
        [InlineKeyboardButton("США", callback_data="USA")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите страну:", reply_markup=reply_markup)
    return COUNTRY

async def choose_country(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    country = query.data
    context.user_data['country'] = country
    await query.message.reply_text(f"Вы выбрали: {country}")

    if country == "Ukraine":
        return await surname_handler.start(update, context)  # Переход к следующему этапу

    # Если выбрана другая страна, можно обработать соответствующим образом
    # Пока обрабатываем только Украину
    return COUNTRY






