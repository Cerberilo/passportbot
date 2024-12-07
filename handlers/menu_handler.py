from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def show_custom_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ['Кнопка 1', 'Кнопка 2'],
        ['Кнопка 3', 'Кнопка 4']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
