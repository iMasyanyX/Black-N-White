import os
from PIL import Image

# Путь к входной и выходной папкам
input_folder = 'in'
output_folder = 'out'

# Создаем выходную папку, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Проходим по всем файлам в входной папке
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpeg', '.jpg')):  # Проверка на расширение файла
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Открываем изображение
        with Image.open(input_path) as img:
            # Преобразуем изображение в черно-белое
            bw_image = img.convert('L')
            # Сохраняем преобразованное изображение в выходной папке
            bw_image.save(output_path)

print("Преобразование завершено.")
