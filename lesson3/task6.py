from random import randint


array = [randint(0, 100) for i in range(randint(4, 12))]
maximum = array[0]
minimum = array[0]
for i in array[1:]:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
index_max, index_min = array.index(maximum), array.index(minimum)
array_sum = 0
if index_max > index_min:
    for i in range(index_min + 1, index_max):
        array_sum += array[i]
else:
    for i in range(index_max + 1, index_min):
        array_sum += array[i]
print(f'{array}\nСумма элементов от минимума до максимума: {array_sum}')
