#  Python 3.8.9, Windows 10 64 bit system


from sys import getsizeof


num = input('Введите любое число: ')
odd = 0
even = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Чётных: {even} Нечётных: {odd}')
print(f'Переременная even весит {getsizeof(even)} байт')  # num = 1235455, getsizeof(even) = 28
#  num = 222222222222222222222222222222222222222222222222222222222222, getsizeof(even) = 28


number = int(input('Введите количество элементов для подсчета суммы ряда: '))
b_n = 1 * (-0.5) ** (number-1)
sum_n = (b_n * (-0.5) - 1) / (-0.5 - 1)
print('Сумма геометрической прогрессии 1 -0.5 0.25 -0.125 ... : ', sum_n)
print(f'Переременная sum_n весит {getsizeof(sum_n)} байт')


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
print(f'Переременная digit весит {getsizeof(digit)} байт\nПереременная k_digit весит {getsizeof(k_digit)} байт')
#  getsizeof(digit) = 50, тк строковая переменная
#  Из всех представленных выше переменных меньше всего места в памяти занимают переменные типа int или float, где
#  целая часть равна 0. Больше всего места занимают строковые переменные, их логичнее было бы хранить как int
#  в данном случае

