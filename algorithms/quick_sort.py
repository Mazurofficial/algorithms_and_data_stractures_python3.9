import math


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = [arr.pop(math.ceil(len(arr) / 2))]
        # print('Опорный элемент: ' + str(pivot))
        less = [i for i in arr if i <= pivot[0]]
        # print('Меньший подмассив: ' + str(less))
        greater = [i for i in arr if i > pivot[0]]
        # print('Больший подмассив: ' + str(greater))
        return quicksort(less) + pivot + quicksort(greater)


array = [11, 223, 2, 1, 32, 45, 21, 3, 45, 3, 3, 54, 22, 100, 111, 23]
print(quicksort(array))
