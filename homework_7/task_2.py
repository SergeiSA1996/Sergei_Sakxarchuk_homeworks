# 2)	Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами. Выведите полученный словарь на экран.

# Способ 1
d = {'1': 0, '2': 0, '3': 0}
print(d)

# Способ 2
d = dict.fromkeys(['1', '2', '3'], 0)
print(d)

# Способ 3
d = {str(i): 0 for i in range(1, 4)}
print(d)
