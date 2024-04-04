# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их
# содержимое в виде одноимённых pickle файлов.

import json
import pickle
from pathlib import Path


def json2pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(f'{file.stem}.pickle', 'wb') as f:
                pickle.dump(data, f)


if __name__ == '__main__':
    json2pickle(Path('/Seminar8_and_HW'))
