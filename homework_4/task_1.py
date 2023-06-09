# 1. Перемножить все нечётные значения в диапазоне от 1 до 100.

pr_vs_ch = 1
for i in range(1, 100):
    if i % 2 != 0:
        pr_vs_ch *= i
print(pr_vs_ch)
