# 4) Дано три числа. Найти количество положительных чисел среди них.

nums_1 = int(input("Введите первое число: "))
nums_2 = int(input("Введите второе  число: "))
nums_3 = int(input("Введите третье число: "))

numberss = 0

if nums_1 > 0:
    numberss += 1
if nums_2 > 0:
    numberss += 1
if nums_3 > 0:
    numberss += 1
print("Колличество положительных чисел равно: ", numberss)
