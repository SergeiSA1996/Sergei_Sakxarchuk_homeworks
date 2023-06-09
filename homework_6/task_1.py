# 1)	Дан список list=[15,48,'hello',6,19,'world’]. Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных. Вывести всё на экран.


list_1 = [15, 48, 'hello', 6, 19, 'world']
glas = ['a', 'e', 'i', 'o', 'u']
for i in range(len(list_1)):
    if isinstance(list_1[i], int):
        if list_1[i] % 2 == 0:
            digits = [int(d) for d in str(list_1[i])]
            list_1[i] = sum(digits)
        else:
            print(f'Заменяем элемент строки {list_1[i]} на {1}')
    elif isinstance(list_1[i], str):
        koll_soglas = 0
        koll_glas = 0
        for letter in list_1[i]:
            if letter.lower() in glas:
                koll_glas += 1
            elif letter.isalpha():
                koll_soglas += 1
        print(f'В слове {list_1[i]} колличество гласных {koll_glas} и колличество согласных {koll_soglas} ')
print(list_1)