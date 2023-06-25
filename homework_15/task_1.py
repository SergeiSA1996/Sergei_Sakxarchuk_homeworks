# 1)	Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны. Валидатором является в программе метод,
# который будет проверять ваши аргументы на то, является ли это число

def validator(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def sum_numbers(a, b):
    if validator(a) and validator(b):
        return float(a) + float(b)
    else:
        raise ValueError("Невалидные данные. Аргументы должны быть числами.")


def subtract_numbers(a, b):
    if validator(a) and validator(b):
        return float(a) - float(b)
    else:
        raise ValueError("Невалидные данные. Аргументы должны быть числами.")


def multiply_numbers(a, b):
    if validator(a) and validator(b):
        return float(a) * float(b)
    else:
        raise ValueError("Невалидные данные. Аргументы должны быть числами.")


def divide_numbers(a, b):
    if validator(a) and validator(b):
        if float(b) != 0:
            return float(a) / float(b)
        else:
            raise ZeroDivisionError("Деление на ноль недопустимо.")
    else:
        raise ValueError("Невалидные данные. Аргументы должны быть числами.")


print(sum_numbers(3, 5))
print(subtract_numbers(10, 4))
print(multiply_numbers(2, 6))
print(divide_numbers(8, 2))
