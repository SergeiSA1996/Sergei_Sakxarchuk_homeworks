# 8) Есть строка ‘Привет, это пример строки в алфавитном порядке',
# необходимо вывести на экран слова в алфавитном порядке


my_str = "Привет, это пример строки в алфавитном порядке"
words = [word.lower() for word in my_str.split()]
words.sort()
for word in words:
    print(word)