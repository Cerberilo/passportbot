from PIL import Image, ImageDraw
from utils.font_utils import get_font
from utils.random_date_generator import generate_random_date
from io import BytesIO

def generate_passport(data: dict) -> BytesIO:
    template = Image.open("templates/passport_template.jpg")
    draw = ImageDraw.Draw(template)
    font = get_font()

    surname_upper = data["surname"].upper()
    name_upper = data["name"].upper()
    patronymic_upper = data["patronymic"].upper()

    draw.text((593, 225), surname_upper, font=font, fill="black")  # Фамилия
    draw.text((593, 330), name_upper, font=font, fill="black")  # Имя
    draw.text((592, 433), patronymic_upper, font=font, fill="black")  # Отчество
    draw.text((596, 500), "Ж/F" if data["gender"] == "F" else "Ч/M", font=font, fill="black")  # Пол

    # Дата рождения
    birth_date = data["birthday"].split("-")
    draw.text((594, 570), birth_date[2], font=font, fill="black")  # День рождения
    draw.text((645, 570), birth_date[1], font=font, fill="black")  # Месяц рождения
    draw.text((694, 570), birth_date[0], font=font, fill="black")  # Год рождения

    # Случайная дата
    random_date = generate_random_date().split(" ")
    draw.text((594, 638), random_date[0], font=font, fill="black")  # Случайный день
    draw.text((645, 638), random_date[1], font=font, fill="black")  # Случайный месяц
    draw.text((694, 638), random_date[2], font=font, fill="black")  # Случайный год

    # Вставка фотографии с адаптацией под нужный размер
    user_photo = Image.open(data["photo"])
    user_photo = user_photo.resize((370, 370), Image.Resampling.LANCZOS)
    template.paste(user_photo, (192, 260))

    output = BytesIO()
    template.save(output, format="JPEG")
    output.seek(0)

    return output







