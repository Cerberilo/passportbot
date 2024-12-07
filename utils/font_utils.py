from PIL import ImageFont

def get_font():
    try:
        return ImageFont.truetype("./fonts/RobotoMono-Light.ttf", 36)
    except FileNotFoundError:
        print("Шрифт не найден, используется стандартный шрифт.")
        return ImageFont.load_default()

