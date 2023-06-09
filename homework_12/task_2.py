# 2) Если в функцию передается кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нем.
# Число - количество нечетных цифр.
# Строка - количество букв.


def count_elements(data):
    if isinstance(data, str):
        return len([c for c in data if c.isalpha()])
    elif isinstance(data, list):
        letters = 0
        odd_digits = 0
        for el in data:
            if isinstance(el, str):
                letters += len([c for c in el if c.isalpha()])
            elif isinstance(el, int):
                odd_digits += len([d for d in str(el) if d.isdigit() and int(d) % 2 != 0])
        return (letters, odd_digits)
    elif isinstance(data, tuple):
        return sum(len(word) for word in data if isinstance(word, str))
    else:
        return "Данный тип данных не поддерживается"