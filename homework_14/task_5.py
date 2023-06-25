# 5. Функция для определения того, является ли строка палиндромом

def is_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False


text = "А роза упала на лапу азора"
result = is_palindrome(text)
if result:
    print(f"Строка '{text}' является палиндромом")
else:
    print(f"Строка '{text}' не является палиндромом")