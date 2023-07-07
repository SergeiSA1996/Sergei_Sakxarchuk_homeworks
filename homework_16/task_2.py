# ) Создайте класс Робот
# создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием
# (может быть несколько и брони может быть несколько. Так же может быть ничего)
# Выведите весь арсенал робота на экран

class Robot:
    def __init__(self, weapons, equipment):
        self.weapons = weapons
        self.equipment = equipment


class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability


class MeleeWeapon(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)


class RangedWeapon(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)


class Equipment:
    def __init__(self, name, protection):
        self.name = name
        self.protection = protection


class Armor(Equipment):
    def __init__(self, name, protection):
        super().__init__(name, protection)


class Helmet(Equipment):
    def __init__(self, name, protection):
        super().__init__(name, protection)


melee_weapon = MeleeWeapon("Меч", 10, 100)
ranged_weapon = RangedWeapon("Автомат", 20, 200)


armor = Armor("Броня", 50)
helmet = Helmet("Шлем", 20)


robot = Robot([melee_weapon, ranged_weapon], [armor, helmet])


print("Оружие:")
for weapon in robot.weapons:
    print(f"Название: {weapon.name}, Урон: {weapon.damage}, Прочность: {weapon.durability}")

print("\nАмуниция:")
for equipment in robot.equipment:
    print(f"Название: {equipment.name}, Защита: {equipment.protection}")
