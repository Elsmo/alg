def quick_sort(nums):  # алгоритм быстрой сортировки
    if len(nums) < 2:
        return nums
    else:
        elem = nums[0]  # опорный элемент
        less = [i for i in nums if i < elem]
        greater = [j for j in nums if j > elem]
        return quick_sort(less) + [elem] + quick_sort(greater)


num = [int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: '))]
print(num)
print(quick_sort(num))
