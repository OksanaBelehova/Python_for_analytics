# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# from datetime import datetime
#
# def is_leap(year: int) -> bool:
#     return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)
#
#
# def valid(full_date: str) -> bool:
#     data, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or data < 1 or data > 31:
#         return False
#     if month in (4, 6, 9, 11) and data > 30:
#         return False
#     if month == 2 and is_leap(year) and data > 29:
#         return False
#     if month == 2 and not is_leap(year) and data > 28:
#         return False
#     else:
#         return True
#
#
# def validate_date(date_):
#     try:
#         datetime.strptime(date_, '%d.%M.%Y')
#         return True
#     except ValueError:
#         return False
#
#
# if __name__ == '__main__':
#     # print(valid('29.02.2024'))
#     date = str(input('Введите дату в формате %d.%M.%Y: '))
#     print(f'Дата может существовать- {valid(date)}')
#     print(f'Дата валидная - {validate_date(date)}')

# 3. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# 4. Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random as rnd

_QUEEN_COUNT: int = 8  # максимальное кол-во ферзей
_SIZE_BOARD: int = 8  # размер доски
_NEED_OK_POSITIONS = 4  # Необходимое кол-во успешных расстановок


def check_queen_8x8(positions: list[tuple]) -> bool:
    """Проверка задачи о ферзях.

    :positions: позиции ферзей - кортежи (строка, столбец)
    """
    result = True

    if len(positions) != _QUEEN_COUNT:
        result = False
    else:
        for i in range(_QUEEN_COUNT - 1):  # берем ферзей по списку, исключая последнего (сам себя бить не может)
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, _QUEEN_COUNT):  # проверяем со следующими до конца списка
                row_2, col_2 = positions[j]
                # Ферзи на одной линии, если координаты строки или столбца у них равны.
                # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением на равное
                # количество строк и столбцов в любую из сторон
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def gen_positions() -> list[tuple[int, int]]:
    """Генератор позиций ферзей. Генерирует _QUEEN_COUNT позиций, по одному ферзю на строку.
    Для доски размером _SIZE_BOARD
    """
    result = []
    for i in range(_SIZE_BOARD):
        result.append((i, rnd.randint(0, _SIZE_BOARD - 1)))
    return result


if __name__ == "__main__":
    queens_positions = [
        [(1, 1), (5, 2), (8, 3), (6, 4), (3, 5), (7, 6), (2, 7), (4, 8)],
        [(0, 5), (1, 2), (4, 3), (2, 2), (7, 6), (5, 1), (2, 7), (3, 4)],
        [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]

    # проверяем шахматы
    for list_position in queens_positions:
        print(list_position)
        if check_queen_8x8(list_position):
            print("Ферзи не бьют друг друга")
        else:
            print("Есть ферзи под ударом")

    # генерация позиций
    total_case_generate = 0  # всего расстановок сгенерировано
    case_ok = 0  # удачных расстановок из всего сгенерированных
    list_ok_positions = []  # список удачных расстановок

    while case_ok < _NEED_OK_POSITIONS:
        generated_position = gen_positions()
        total_case_generate += 1
        if check_queen_8x8(generated_position):
            case_ok += 1
            list_ok_positions.append(generated_position)

    print(f" Всего сгенерировано {total_case_generate}, удачные:")
    for pos in list_ok_positions:
        print(pos)
