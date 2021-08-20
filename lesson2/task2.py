num = input('Введите любое число: ')
odd = 0
even = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Чётных: {even} Нечётных: {odd}')
