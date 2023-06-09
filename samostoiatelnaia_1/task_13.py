# 13.	Дан список чисел, необходимо удалить все вхождения числа 20 из него.

list_1 = [5, 20, 15, 20, 25, 50, 20]
namber = 20
while namber in list_1:
    list_1.remove(namber)
print(list_1)
