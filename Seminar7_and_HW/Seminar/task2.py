# Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с
# заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть
# гласные. Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def set_name(count: int, file: str | Path) -> None:
    with open(file, 'a', encoding='utf-8') as f:
        for _ in range(count):
            name = ''.join(
                choice(CONSONANTS) if i not in (1, 4, 6) else choice(VOWELS) for i in range(randint(MIN_LEN, MAX_LEN)))
            print(name.capitalize(), file=f)


if __name__ == '__main__':
    set_name(120, Path('names.txt'))
