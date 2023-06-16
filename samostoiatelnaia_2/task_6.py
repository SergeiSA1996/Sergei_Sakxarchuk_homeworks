#6.	Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.


def compress_array(arr, a, b):
    size = len(arr)
    compressed_arr = []
    for i in range(size):
        if arr[i] < a or arr[i] > b:
            compressed_arr.append(arr[i])
    compressed_size = len(compressed_arr)
    arr[compressed_size:] = [0] * (size - compressed_size)
    return compressed_arr + [0] * (size - compressed_size)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 3
b = 7

compressed_array = compress_array(array, a, b)
print("Сжатый массив:", compressed_array)
