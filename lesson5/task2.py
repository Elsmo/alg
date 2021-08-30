from collections import defaultdict
from collections import deque


def to_dec(hex_num):
    dec = 0
    num = deque(hex_num)
    num.reverse()
    for j in range(len(num)):
        dec += table[num[j]] * 16 ** j
    return dec


def to_hex(dec_num):
    num = deque()
    while dec_num > 0:
        d = dec_num % 16
        for j in table:
            if table[j] == d:
                num.append(j)
        dec_num //= 16
    num.reverse()
    return list(num)


table = defaultdict(int)
cnt = 0
for i in '0123456789ABCDEF':
    table[i] += cnt
    cnt += 1

num_1 = to_dec(input('Первое шестнадцатиричное число: ').upper())
num_2 = to_dec(input('Второе шестнадцатиричное число: ').upper())

print(f'Сумма чисел: {to_hex(num_1 + num_2)}')
print(f'Произведение чисел: {to_hex(num_1 * num_2)}')
