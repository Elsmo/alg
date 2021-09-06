import random


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    left_side = merge_sort(arr[:len(arr) // 2])
    right_side = merge_sort(arr[len(arr) // 2:])

    i = j = 0
    res = []

    while i < len(left_side) or j < len(right_side):

        if i >= len(left_side):
            res.append(right_side[j])
            j += 1

        elif j >= len(right_side):
            res.append(left_side[i])
            i += 1

        elif left_side[i] < right_side[j]:
            res.append(left_side[i])
            i += 1

        else:
            res.append(right_side[j])
            j += 1

    return res


my_array = [round(random.uniform(0, 50), 2) for i in range(10)]

print(f'Исходный массив:\n{my_array}')
print(f'Сортированный массив:\n{merge_sort(my_array)}')
