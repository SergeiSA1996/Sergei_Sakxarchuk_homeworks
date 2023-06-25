# 1.Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
# Написать программу, со следующим интерфейсом:
# пользователю предоставляется на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.


def inches_to_cm(value):
    return value * 2.54


def cm_to_inches(value):
    return value / 2.54


def miles_to_km(value):
    return value * 1.60934


def km_to_miles(value):
    return value / 1.60934


def pounds_to_kg(value):
    return value * 0.453592


def kg_to_pounds(value):
    return value / 0.453592


def ounces_to_grams(value):
    return value * 28.3495


def grams_to_ounces(value):
    return value / 28.3495


def gallons_to_liters(value):
    return value * 3.78541


def liters_to_gallons(value):
    return value / 3.78541


def pints_to_liters(value):
    return value * 0.473176


def liters_to_pints(value):
    return value / 0.473176


def main():
    while True:
        print("Выберите вариант перевода:")
        print("1. Дюймы в сантиметры")
        print("2. Сантиметры в дюймы")
        print("3. Мили в километры")
        print("4. Километры в мили")
        print("5. Фунты в килограммы")
        print("6. Килограммы в фунты")
        print("7. Унции в граммы")
        print("8. Граммы в унции")
        print("9. Галлон в литры")
        print("10. Литры в галлоны")
        print("11. Пинты в литры")
        print("12. Литры в пинты")
        print("0. Выход")

        choice = int(input("Введите номер: "))

        if choice == 0:
            print("Выход из программы.")
            break

        value = float(input("Введите значение: "))

        if choice == 1:
            result = inches_to_cm(value)
            print(f"{value} дюймов = {result} сантиметров")
        elif choice == 2:
            result = cm_to_inches(value)
            print(f"{value} сантиметров = {result} дюймов")
        elif choice == 3:
            result = miles_to_km(value)
            print(f"{value} миль = {result} километров")
        elif choice == 4:
            result = km_to_miles(value)
            print(f"{value} километров = {result} миль")
        elif choice == 5:
            result = pounds_to_kg(value)
            print(f"{value} фунтов = {result} килограммов")
        elif choice == 6:
            result = kg_to_pounds(value)
            print(f"{value} килограммов = {result} фунтов")
        elif choice == 7:
            result = ounces_to_grams(value)
            print(f"{value} унций = {result} граммов")
        elif choice == 8:
            result = grams_to_ounces(value)
            print(f"{value} граммов = {result} унций")
        elif choice == 9:
            result = gallons_to_liters(value)
            print(f"{value} галлонов = {result} литров")
        elif choice == 10:
            result = liters_to_gallons(value)
            print(f"{value} литров = {result} галлонов")
        elif choice == 11:
            result = pints_to_liters(value)
            print(f"{value} пинт = {result} литров")
        elif choice == 12:
            result = liters_to_pints(value)
            print(f"{value} литров = {result} пинт")
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


main()