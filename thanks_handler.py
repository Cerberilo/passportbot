from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def send_thanks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаем кнопки для копирования номера кошелька
    keyboard = [
        [InlineKeyboardButton("Копировать USDT", callback_data="copy_usdt")],
        [InlineKeyboardButton("Копировать Binance Pay", callback_data="copy_binance")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Сообщение с благодарностью и информацией о донате
    message = (
        "Спасибо что воспользовались ботом! Надеюсь, был полезен. "
        "Вы можете поддержать автора этого бота донатом.\n\n"
        "USDT:\n"
        "номер кошелька (нажмите, чтобы скопировать)\n\n"
        "Binance Pay:\n"
        "номер Binance Pay (нажмите, чтобы скопировать)"
    )

    await update.message.reply_text(message, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Обработка нажатий на кнопки
    if query.data == "copy_usdt":
        await query.message.reply_text("Номер кошелька USDT скопирован!")
    elif query.data == "copy_binance":
        await query.message.reply_text("Номер Binance Pay скопирован!")
