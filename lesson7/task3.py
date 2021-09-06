import random


def quick_sort(nums):  # быстрая сортировка
    if len(nums) < 2:
        return nums
    else:
        elem = nums[0]  # опорный элемент
        less = [i for i in nums if i < elem]
        greater = [j for j in nums if j > elem]
        return quick_sort(less) + [elem] + quick_sort(greater)


my_arr = [random.randint(0, 100) for i in range(2 * 5 + 1)]

sorted_arr = quick_sort(my_arr)
if len(my_arr) % 2 == 0:
    avg = (sorted_arr[len(my_arr) // 2] + sorted_arr[(len(my_arr) // 2) - 1]) / 2
else:
    avg = sorted_arr[len(my_arr) // 2]

print(f'Исходный массив:\n{my_arr}')
print(f'Отсортированный массив:\n{sorted_arr}')
print(f'Медиана массива: {avg}')
