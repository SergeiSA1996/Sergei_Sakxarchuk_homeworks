# Ввести 10 чисел с клавиатуры, данные числа добавить во множество.


numbers_set = set()
for _ in range(10):
    number = int(input("Введите число: "))
    numbers_set.add(number)
print("Множество чисел:", numbers_set)