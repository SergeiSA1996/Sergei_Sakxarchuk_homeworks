# 15.Необходимо удалить пустые строки из списка строк.


stroka_1 = ['hello my friend', 'my name is',"", 'house', 'cat', 'dog', '']

res = [mystr for mystr in stroka_1 if mystr]
print(res)
