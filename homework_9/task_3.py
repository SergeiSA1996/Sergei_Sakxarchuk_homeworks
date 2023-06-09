# 3)	В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.


with open('now_bad.txt') as f:
    lines = f.readlines()
    print('Количество строк в файле:', len(lines))
    for i, line in enumerate(lines):
        print(f'Количество символов в строке {i + 1}:', len(line.strip()))
