# 4. Функция для определения всех чисел, на которые без остатка делится указанное

def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


num = 24
result = get_divisors(num)
print(f"Все числа, на которые число {num} делится без остатка: {result}")