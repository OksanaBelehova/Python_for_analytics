# 1. Напишите функцию для транспонирования матрицы
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# def transpose(matrix):
#     rows = len(matrix)
#     colms = len(matrix[0])
#     transpos_matrix = [[0 for _ in range(rows)] for _ in range(colms)]
#     for i in range(rows):
#         for j in range(colms):
#             transpos_matrix[j][i] = matrix[i][j]
#     return transpos_matrix
#
# print(transpose(matrix))

# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# def create_dict(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         try:
#             result[value] = key
#         except:
#             result[str(value)] = key
#     return result
#
# print(create_dict(name='Иван', sername='Иванов', weight=35.5,
#                      months=['January', 'February', 'March'],
#                      courses={'python': 'ver 3.11', 'c#': 'ver 2.5'}))

# 3. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Напишите программу банкомат.
# ● Начальная сумма равна нулю
# ● Допустимые действия: пополнить, снять, выйти
# ● Сумма пополнения и снятия кратны 50 у.е.
# ● Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ● После каждой третей операции пополнения или снятия начисляются проценты -
# 3%
# ● Нельзя снять больше, чем на счёте
# ● При превышении суммы в 5 млн, вычитать налог на богатство 10% перед
# каждой операцией, даже ошибочной
# ● Любое действие выводит сумму денег

import decimal
from datetime import date

CMD_DEPOSIT = 'п'
CMD_WITHDRAU = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10)/decimal.Decimal(100)
WITDRAW_PERCENT = decimal.Decimal(15)/decimal.Decimal(1000)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
percent_add = 0.03

bank = decimal.Decimal(0)
count = 0
def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * WITDRAW_PERCENT < MIN_REMOVAL:
        bank -= MIN_REMOVAL
        print("списаны проценты за cash: ", MIN_REMOVAL)
    elif cash * WITDRAW_PERCENT > MAX_REMOVAL:
        bank -= MAX_REMOVAL
        print("списаны проценты за cash: ", MAX_REMOVAL)
    else:
        bank -= cash * WITDRAW_PERCENT
        print("списаны проценты за cash: ", cash * WITDRAW_PERCENT)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % MULTIPLICITY == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > RICHNESS_SUM:
            bank = bank - bank * RICHNESS_TAX
            print("списан налог на богатство: ", bank * RICHNESS_TAX)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > RICHNESS_SUM:
            bank = bank - bank * RICHNESS_TAX
            print("списан налог на богатство: ", bank * RICHNESS_TAX)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > RICHNESS_SUM:
            bank = bank - bank * RICHNESS_TAX
            print("списан налог на богатство: ", bank * RICHNESS_TAX)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
