# 1) При заданном целом числе n посчитайте n + nn + nnn.

n = int(input("Введите число n:"))
result = n + n*10+n + n*100+n*10+n
print("n + nn + nnn = ", result)