import random


def bubble_sort(arr):

    for i in range(len(arr) - 1):
        cnt = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
        if cnt == 0:
            break
    return arr


my_array = [random.randint(-100, 99) for i in range(10)]

print(f'Исходный массив:\n{my_array}')
print(f'Отсортированный массив:\n{bubble_sort(my_array)}')
