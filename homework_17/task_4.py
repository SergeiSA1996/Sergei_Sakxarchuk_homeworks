# 4) Исходные данные:
# - скрипт task1, который содержит реализацию классов Tank, TankCommander, TankGunner и
# код для проверки результата
#
# Необходимо:
# 1. Реализовать всю необходимую логику так, чтобы скрипт task1 выводил:
#     >>> Test passed. Amazing job!
#
# Желательно:
# 1. Привести альтернативные способы решения задачи.
#
# Примечание:
# - НЕЛЬЗЯ менять реализацию приведенных в исходных данных классов и проверочного кода.
# - Нет ограничений по реализации классов Tankman и Vehicle, а также вспомогательной логики.

class Tank:
    def __init__(self, name, commander, gunner):
        self.name = name
        self.commander = commander
        self.gunner = gunner


class TankCommander(Tankman):
    def target(self):
        print("Target acquired!")

    def fire(self):
        print("Fire!")


class TankGunner(Tankman):
    def aim(self):
        print("Aiming...")

    def fire(self):
        print("Firing...")


class Tankman:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank


class Vehicle:
    def __init__(self, name, crew):
        self.name = name
        self.crew = crew


tankman1 = Tankman("John", "Corporal")
tankman2 = Tankman("Mike", "Sergeant")

tank = Tank("T-34", tankman1, tankman2)
tank.commander.target()
tank.gunner.aim()
tank.commander.fire()
tank.gunner.fire()

vehicle = Vehicle("Truck", [tankman1, tankman2])

if isinstance(vehicle, Vehicle) and isinstance(tank, Tank):
    print("Test passed. Amazing job!")
else:
    print("Test failed. Try again.")