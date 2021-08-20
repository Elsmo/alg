n_num = input('Сколько чисел будет введено:  ')
digit = input('Какую цифру ищем: ')
k_digit = 0
n = 0
while n < int(n_num):
    user_num = input('Введите число: ')
    for i in user_num:
        if i == digit:
            k_digit += 1
    n += 1
print(f'Цифра {digit} была введена {k_digit} раз')