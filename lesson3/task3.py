from random import randint


array = [randint(0, 100) for i in range(randint(4, 12))]
maximum = array[0]
minimum = array[0]
for i in array[1:]:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print('Исходный список:', array)
index_max, index_min = array.index(maximum), array.index(minimum)
array[index_min], array[index_max] = array[index_max], array[index_min]
print('Итоговый список:', array)
