k = 0
for i in range(2, 99):
    for j in [2, 3, 4, 5, 6, 7, 8, 9]:
        if i % j == 0:
            k += 1
print(f'{k} чисел последовательности кратны цифрам от 2 до 9')
