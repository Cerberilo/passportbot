from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from handlers import surname_handler, name_handler, patronymic_handler, gender_handler, date_handler, photo_handler

SURNAME, NAME, PATRONYMIC, GENDER, PHOTO, CALENDAR = range(6)

async def restart(update, context):
    """Функция для перезапуска диалога"""
    await update.message.reply_text("Перезапуск діалогу...")
    return await surname_handler.start(update, context)

def main():
    application = ApplicationBuilder().token("7470905747:AAEK-iBsLKsYsVSXTE2hB6I5JWyUZXoAsgs").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", surname_handler.start)],
        states={
            SURNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, surname_handler.surname)],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name_handler.name)],
            PATRONYMIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, patronymic_handler.patronymic)],
            CALENDAR: [CallbackQueryHandler(date_handler.calendar_handler)],
            GENDER: [CallbackQueryHandler(gender_handler.gender_handler)],
            PHOTO: [MessageHandler(filters.PHOTO, photo_handler.photo)],
        },
        fallbacks=[
            CommandHandler("cancel", surname_handler.cancel),
            CommandHandler("restart", restart)  # Добавляем обработчик команды /restart
        ],
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()





















