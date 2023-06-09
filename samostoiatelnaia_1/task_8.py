# 8.Вам передан массив чисел.
# Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5


# a = [1, 5, 2, 9, 2, 9, 1]
# print(min(a, key=a.count))


a = [1, 5, 2, 9, 2, 9, 1]
real_min = a[0]
min_count = a.count(real_min)
for i in a:
    if a.count(i) < min_count:
        real_min = i
        break
print(real_min)