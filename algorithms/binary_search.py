import math


def binary_search(a_list, list_item):
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = math.ceil((low + high) / 2)
        guess = list[mid]
        if guess == list_item:
            return mid
        if guess > list_item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 7, 8, 9, 11]
item = int(input("Enter item to search: "))
print('Address of item = ' + str(binary_search(my_list, item)))
