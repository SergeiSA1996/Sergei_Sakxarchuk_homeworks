# 4) Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:
# •	количество букв латинского алфавита;
# •	число слов;
# •	число строк.
# Пример ввода и вывода
# Предположим, что file.txt содержит приведенный ниже текст:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.


with open("file.txt") as f:
    text = f.read()
num_letters = sum(1 for char in text if char.isalpha())
num_words = len(text.split())
num_lines = text.count("\n") + 1
print(f"Количество букв: {num_letters}")
print(f"Число слов: {num_words}")
print(f"Число строк: {num_lines}")