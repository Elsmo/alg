import time
from random import randint


start_time = time.time()


def quick_sort(nums):  # алгоритм быстрой сортировки это О(n*logn)
    if len(nums) < 2:
        return nums
    else:
        elem = nums[0]
        less = [i for i in nums if i < elem]
        greater = [j for j in nums if j > elem]
        return quick_sort(less) + [elem] + quick_sort(greater)


num = [randint(0, 100) for i in range(randint(100, 250))]
print(num)
print(quick_sort(num))
print("--- %s seconds ---" % (time.time() - start_time))  # в среднем 0.0010008811950683594 seconds


# def array_minimum(arr):  # поиск минимума для реализации сортировки выбором
#     minimum = arr[0]
#     ind_minimum = arr.index(minimum)
#     for i in arr[1:]:
#         if i < minimum:
#             minimum = i
#             ind_minimum = arr.index(minimum)
#     return ind_minimum
#
#
# def selection_sort(nums):  # сортировка выбором это О(n**2)
#     nums_sort = []
#     for i in range(len(nums)):
#         smallest = array_minimum(nums)
#         nums_sort.append(nums.pop(smallest))
#     return nums_sort
#
#
# num = [randint(0, 100) for i in range(randint(100, 250))]
# print(num)
# print(selection_sort(num))
# print("--- %s seconds ---" % (time.time() - start_time))  # в среднем 0.0019965171813964844 seconds
