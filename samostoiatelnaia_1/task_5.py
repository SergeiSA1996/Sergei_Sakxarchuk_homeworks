# 5.Даны два целых числа m и n.
# Напишите программу,которая выводит все числа от m до n включительно в порядке возрастания,
# если m < n, или в порядке убывания в противном случае.


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

if num_1 < num_2:
    for spis in range(num_1, num_2 + 1):
        print(spis)
else:
    for spis in range(num_1, num_2 - 1, -1):
        print(spis)