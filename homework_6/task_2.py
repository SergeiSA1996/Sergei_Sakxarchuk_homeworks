# 2)	Даны 2 списка: a = [4,6,'pу','tell',78] b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции: 1)Сложить два списка 2) Добавьте элемент 6 на 3 позицию.
# 3)Удалите все текстовые переменные 4) Посчитайте количество элементов списка


a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]

c = a + b
print(c)
c.insert(3, 6)
print(c)
c.pop(2)
c.pop(3)
c.pop(5)
c.pop(6)
print(c)
print(len(c))
