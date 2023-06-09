# 2. Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и вывести на экран.
# Затем объединить элементы с использованием пробела, чтобы программа вывела “Apples Oranges Pears Bananas Berries”.

stroka_1 = 'Apples, Oranges, Pears, Bananas, Berries'
stroka_s_zap = stroka_1.split()
print(stroka_s_zap)
stroka_2 = ''.join(stroka_1)
stroka_s_prob = stroka_1.replace(',', ' ')
print(stroka_s_prob)
