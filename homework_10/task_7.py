# 7) Есть строка со знаками препинания. Удалить из строки знаки препиныния.


import string

text = 'Это текст со знаками препинания, например, запятой и точки!'
for punctuation in string.punctuation:
    text = text.replace(punctuation, '')
print(text)
