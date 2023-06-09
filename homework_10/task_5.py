# 5) Сгенерировать список используя генератор списков.
# В списке должно быть 10 элементов в произвольном случайном диапазоне.
# Перевести все числа в строку и получить из списка -  строку.


import random

random_list = [random.randint(1, 100) for _ in range(10)]
str_list = [str(num) for num in random_list]
result_string = ''.join(str_list)
print(result_string)
