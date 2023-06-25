#  7. Напишите функцию, которая определяет количество гласных в строке


def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


text = "Hello world"
result = count_vowels(text)
print(f"Количество гласных в строке '{text}' равно {result}")