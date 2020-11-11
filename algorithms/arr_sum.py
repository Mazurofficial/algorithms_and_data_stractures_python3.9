def arr_sum(arr):
    array_sum = 0

    if len(arr) == 0:
        return 0
    elif len(arr) > 0:
        array_sum = arr.pop(0) + arr_sum(arr)
    return array_sum


array = [1, 2, 4, 6, 90, 21, 34]
print(arr_sum(array))
