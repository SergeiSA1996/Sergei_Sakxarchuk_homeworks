#Создать множество.
# Создать неизменяемое множество.
# Выполнить операцию объединения созданных множеств.
# Выполнить операцию пересечения созданных множеств.


# создание множества
my_set = {1, 2, 3, 4, 5}
print("Множество:", my_set)

# создание неизменяемого множества
frozen_set = frozenset([4, 5, 6, 7, 8])
print("Неизменяемое множество:", frozen_set)

# объединение множеств
union_set = my_set.union(frozen_set)
print("Объединение множеств:", union_set)

# пересечение множеств
intersection_set = my_set.intersection(frozen_set)
print("Пересечение множеств:", intersection_set)