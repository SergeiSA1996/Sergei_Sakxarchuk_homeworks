#2. Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.


from math import sqrt
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

Sred_A = (num_1+num_2)/2
Sred_G = sqrt(num_1 * num_2)
print("Среднее арифметическое двух чисел равно: ", float(Sred_A), "Среднее Геометрическое двух чисел равно: ", float(Sred_G))