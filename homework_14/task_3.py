# 3. Необходимо написать функцию findnextsquare,
# который находит следующий целочисленный идеальный квадрат после квадрата, переданного в качестве параметра.
# Напомним, что целочисленный квадрат - это число n, такое что sqrt (n) также является целым числом.
# Если параметр сам по себе не является идеальным квадратом -1,
# его следует вернуть(вернуть -1 если введенное нами число не является квадратом)
# 121 —> 144
# 625 —> 676


import math


def find_next_square(square):
    if math.sqrt(square) % 1 != 0:
        return -1
    number = math.isqrt(square) + 1
    while True:
        if math.isqrt(number) ** 2 == number:
            return number
        number += 1


print(find_next_square(121))
print(find_next_square(625))