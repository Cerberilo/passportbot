from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from utils.passport_generator import generate_passport
from PIL import Image, ImageEnhance
from io import BytesIO
import random

def apply_random_filters(image):
    """Применяет случайные фильтры яркости и контрастности к изображению."""
    # Рандомное значение для яркости
    brightness_factor = random.uniform(0.8, 1.2)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

    # Рандомное значение для контрастности (также сужаем диапазон)
    contrast_factor = random.uniform(0.8, 1.2)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    return image

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        photo_bytes = BytesIO(await photo_file.download_as_bytearray())
        context.user_data["photo"] = photo_bytes

        passport_image = generate_passport(context.user_data)

        # Загрузка изображения из BytesIO
        passport_image = Image.open(passport_image)

        # Применение случайных фильтров
        passport_image = apply_random_filters(passport_image)

        # Сохранение финального изображения в байтовый поток для отправки
        output = BytesIO()
        passport_image.save(output, format="JPEG")
        output.seek(0)

        await update.message.reply_photo(photo=output)
        await update.message.reply_text("Дякую, що скористалися ботом. Сподіваємось він був корисний вам😊")
        await update.message.reply_text("Якщо хочете створити ще один документ, натисніть /start")

        return ConversationHandler.END
    else:
        await update.message.reply_text("Будь ласка, надішліть фотографію")
        return 4  # PHOTO






