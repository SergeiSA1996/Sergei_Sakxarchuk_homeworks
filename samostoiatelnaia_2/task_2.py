#2.	Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.


def find_elements_less_than_average(lst):
    average = sum(lst) / len(lst)
    result = []
    for elem in lst:
        if elem < average:
            result.append(elem)
    return result
lst = [1, 2, 3, 4, 5]
elements_less_than_average = find_elements_less_than_average(lst)
print(elements_less_than_average)