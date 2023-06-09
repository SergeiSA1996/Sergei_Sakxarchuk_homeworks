# 1)Есть список состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины,
# а после слов цифры в порядке возрастания.

spis_1 = ['My', 1, 4, 7, 8, 'cat', 'dog']

words_list = [x for x in spis_1 if isinstance(x, str)]
numbers_list = [x for x in spis_1 if isinstance(x, int)]
words_list_sorted = sorted(words_list, key=len)
numbers_list_sorted = sorted(numbers_list)
with open('spis_1.txt', 'w') as f:
    f.write('\n'.join(words_list_sorted))
    f.write('\n')
    f.write('\n'.join([str(x) for x in numbers_list_sorted]))
