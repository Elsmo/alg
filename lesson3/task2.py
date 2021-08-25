from random import randint


array_original = [randint(0, 100) for i in range(randint(3, 12))]
array_new = []
for n in range(len(array_original)):
    if array_original[n] % 2 == 0:
        array_new.append(n+1)
print(f'Начальный массив: {array_original}\nМассив с индексами четных элементов: {array_new}')
