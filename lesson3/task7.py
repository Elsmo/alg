from random import randint


def find_min(a):
    a_min = a[0]
    for i in a[1:]:
        if i < a_min:
            a_min = i
    return a_min


array = [randint(0, 100) for i in range(randint(4, 12))]
print(array)
minimum_first = find_min(array)
array.remove(minimum_first)
minimum_second = find_min(array)
print(f'Наименьшие элементы массива: {minimum_first}, {minimum_second}')
