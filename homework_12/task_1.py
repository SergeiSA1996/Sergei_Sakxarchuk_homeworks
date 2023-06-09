# 1)	Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку:
# “Деление на ноль” Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


def summ_nubers(num_1, num_2):
    return num_1 + num_2


def vich_numbers(num_1, num_2):
    return num_1 - num_2


def umnoz_numbers(num_1, num_2):
    return num_1 * num_2


def dele_numbers(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print('Ошибка, деление на 0')


while True:
    parametr = input("Введите необходимую операцию для работы '+', '-', '*', '/' ,'0 - для завершения работы': ")
    if parametr == '+':
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите вотрое число: "))
        print(f"Сумма чисел: {summ_nubers(num_1, num_2)}")
    elif parametr == '-':
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите вотрое число: "))
        print(f"Разность чисел: {vich_numbers(num_1, num_2)}")
    elif parametr == '+':
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите вотрое число: "))
        print(f"Произведение чисел: {umnoz_numbers(num_1, num_2)}")
    elif parametr == '/':
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите вотрое число: "))
        print(f"Деление чисел: {dele_numbers(num_1, num_2)}")
    elif parametr == '0':
        print("Спасибо за работу, операции завершены")
        break
