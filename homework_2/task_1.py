# 1. Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.


my_stroka = 'Hello my name is Sergei'
print(my_stroka[3])
print(my_stroka[-2])
print(my_stroka[:5])
print(my_stroka[:-2])
print(my_stroka[::2])
print(my_stroka[1::2])
print(my_stroka[::-1])
print(my_stroka[::-2])
print(len(my_stroka))
