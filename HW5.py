# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# import os
#
# string = 'D:\Data\MyFiles\mile.png'
#
# def path_fun(f_path: str) -> tuple:
#     filepath, file_extension = os.path.splitext(f_path)
#     dirname, filename = os.path.split(filepath)
#     return (dirname, filename, file_extension)
#
# print(f'Исходная строка: {string} \nКортеж из пути: {path_fun(string)}')

# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# def generate_salary_dict(names_list, salaries_list, bonuses_list):
#     return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}
#
# names = ["Ivan", "Alex", "Nick"]
# salaries = [40000, 50000, 80000]
# bonuses = ["10.25%", "13.5%", "18%"]
#
# salary_dict = generate_salary_dict(names, salaries, bonuses)
# print(salary_dict)

# 4. Создайте функцию генератор чисел Фибоначчи
# ttps://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

a = int(input('Введите число элеменов Фибоначчи '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))
