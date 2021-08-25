from random import randint


array = [randint(-50, 50) for i in range(randint(4, 12))]
max_negative = sorted(array)[0]
max_negative_index = 0
for i in range(len(array)):
    if 0 > array[i] > max_negative:
        max_negative = array[i]
        max_negative_index = i
print(f'Массив: {array}\nМаксимальный отрацательный элемент {max_negative} стоит на позиции {max_negative_index+1}')
