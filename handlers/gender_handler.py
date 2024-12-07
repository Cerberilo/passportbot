from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def send_gender_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Ж/F", callback_data="F"), InlineKeyboardButton("Ч/M", callback_data="M")]
    ]
    query = update.callback_query
    await query.edit_message_text("Оберіть стать👥 :", reply_markup=InlineKeyboardMarkup(keyboard))

async def gender_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    context.user_data["gender"] = query.data
    await query.message.reply_text(f"Вы обрали стать: {'Жінка' if query.data == 'F' else 'Чоловік'}")

    # Создаем кнопку с ссылкой
    button = [
        [InlineKeyboardButton("Або перейдіть на сайт генерація фото", url='https://thispersondoesnotexist.com/')]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    await query.message.reply_text("📎Надішліть фотографію:", reply_markup=reply_markup)
    return 4  # PHOTO

