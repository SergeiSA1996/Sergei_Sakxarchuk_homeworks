# 5)	Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице


list_1 = []
for i in range(100):
    list_1.append('0')
list_1[0] = '1'
list_1[-1] = '1'
print(list_1)
