from random import randint
from operator import itemgetter


array = [randint(0, 25) for i in range(randint(10, 12))]
k = 0
new_array = []
for i in range(len(array)):
    for j in range(len(array)):
        if array[j] == array[i]:
            k += 1
    new_array.append((array[i], k))
    k = 0
new_array = sorted(new_array, key=itemgetter(1), reverse=True)
print(f'В исходном массиве: {array}\nчаще всего встречается {new_array[0][0]}')
