# 1)	Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# apple = Apple("sort", [a,b,c], 120, "apple")
# apple.clear()
# >>"apple очищен"

class Fruit:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

    def __str__(self):
        return f"Сорт - {self.sort}, Витамины - {self.vitamins}, Цена - {self.price}, Имя - {self.name}"


class Orange(Fruit):
    def clear(self):
        print(f"{self.name} очищен")


class Apple(Fruit):
    def cut(self):
        print(f"{self.name} порезан")


class Mandarin(Fruit):
    def clear(self):
        print(f"{self.name} очищен")


class Banana(Fruit):
    def __init__(self, sort, vitamins, price, name, potassium):
        super().__init__(sort, vitamins, price, name)
        self.potassium = potassium

    def clear(self):
        print(f"{self.name} очищен")


orange = Orange("апельсинный", ["витамин C"], 50, "апельсин")
apple = Apple("зеленое яблоко", ["витамин A", "витамин C"], 30, "яблоко")
mandarin = Mandarin("гавайская", ["витамин C"], 40, "мандарин")
banana = Banana("тайский", ["витамин B6", "витамин C"], 60, "банан", "высокое")

orange.clear()
apple.cut()
mandarin.clear()
banana.clear()

print(orange)
print(apple)
print(mandarin)
print(banana)