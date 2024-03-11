# 2. Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# HEX = 16
#
# hex_digits = "0123456789abcdef"
# num = int(input('Введите целое число: '))
# result: str = ''
# test_num: int = num
# while test_num > 0:
#     result = hex_digits[test_num % HEX] + result
#     test_num //= HEX
# print(f'Число в шестнадцатиричной системе {result}')
#
# print(f'Проверка функцией hex {hex(num)}')

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction as F

num1 = input('Введите первую дробь вида a/b: ')
num2 = input('Введите вторую дробь вида a/b: ')

print(num1, '+', num2, '=', F(num1)+F(num2))
print(num1, '*', num2, '=', F(num1)*F(num2))

# Преобразуем дроби из строк в числа
num1_, denom1 = map(int, num1.split("/"))
num2_, denom2 = map(int,snum2.split("/"))

# Сумма дробей
sum_num = num1_ * denom2 + num2_*denom1
sum_denom = denom1*denom2

# Произведение дробей
comp_num = num1_ * num2_
comp_denom = denom1*denom2

print(f"Сумма дробей {num1} и {num2} - {sum_num}/{sum_denom}")
print(f"Произведение дробей {num1} и {num2} - {comp_num}/{comp_denom}")
