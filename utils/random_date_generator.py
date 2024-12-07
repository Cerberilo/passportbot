import random

def generate_random_date():
    day = str(random.randint(1, 31)).zfill(2)  # Рандомный день от 1 до 31
    month = str(random.randint(1, 12)).zfill(2)  # Рандомный месяц от 1 до 12
    year = "2028"  # Фиксированный год 2028

    return f"{day} {month} {year}"

