# 4) Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.


s = "abracadabra"
unique_set = set(s)
result = tuple("".join(unique_set))
print(result)
