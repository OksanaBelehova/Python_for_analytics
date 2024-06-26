# 2. Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.


import HW8.HW8 as di

JSON_FILENAME = "info.json"
CSV_FILENAME = "info.csv"
PICK_FILENAME = "info.pcl"

if __name__ == '__main__':
    print("Информация о каталоге: ")
    dir_info = di.dir_info()  # сканируем текущий каталог
    print(dir_info)
    # Сохраняем в различные форматы
    print("Сохранение информации в файлы")
    di.save_to_json(dir_info, JSON_FILENAME)
    di.save_to_picle(dir_info, PICK_FILENAME)
    di.save_to_csv(dir_info, CSV_FILENAME)

    print(f"Информация в файлах: {JSON_FILENAME}, {CSV_FILENAME}, {PICK_FILENAME}")
