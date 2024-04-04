# Мы сформировали текстовый файл с
# псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в
# формате JSON. Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки


import json
from pathlib import Path


def convert(file: Path) -> None:
    data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            data[name.capitalize()] = float(number)
        with open(file.stem + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    convert(Path('/Seminar7_and_HW/Seminar/results.txt'))
