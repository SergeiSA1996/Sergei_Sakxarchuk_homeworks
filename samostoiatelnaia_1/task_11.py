# 11.	Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.


stroka_1 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']

res = [mystr for mystr in stroka_1 if " " in mystr]
print(res)


