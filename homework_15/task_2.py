# 2)Функция sum(a,b) принимает 2 числа и возвращает их сумму. Написать декоратор,
# который возвращает ошибку если переданы не числовые параметры(например строка)


def validate_int_parameters(func):
    def wrapper(a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Ошибочные параметры: оба параметра должны быть числами.")
        return func(a, b)
    return wrapper


@validate_int_parameters
def summ(a, b):
    return a + b


