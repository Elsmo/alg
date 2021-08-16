def to_binary(num):
    bin_num = ''
    while num > 0:
        bin_num = str(num % 2) + bin_num
        num = num // 2
    return bin_num


def to_decimal(bin_num):
    dec_num = 0
    while len(bin_num) > 0:
        dec_num += int(bin_num[0]) * (2 ** (len(bin_num)-1))
        bin_num = bin_num[1:]
    return dec_num


def bitwise_or(bin_a, bin_b):  # побитовое ИЛИ
    res = ''
    if len(bin_a) == len(bin_b):
        for i in range(len(bin_a)):
            if bin_a[i] == '0' and bin_b[i] == '0':
                res += '0'
            else:
                res += '1'
        return res
    else:
        if len(bin_a) > len(bin_b):
            bin_b += '0' * abs(len(bin_a)-len(bin_b))
            return bitwise_or(bin_a, bin_b)
        else:
            bin_a += '0' * abs(len(bin_a)-len(bin_b))
            return bitwise_or(bin_a, bin_b)


def bitwise_and(bin_a, bin_b):  # побитовое И
    res = ''
    if len(bin_a) == len(bin_b):
        for i in range(len(bin_a)):
            if bin_a[i] == '1' and bin_b[i] == '1':
                res += '1'
            else:
                res += '0'
        return res
    else:
        if len(bin_a) > len(bin_b):
            bin_b += '0' * abs(len(bin_a) - len(bin_b))
            return bitwise_and(bin_a, bin_b)
        else:
            bin_a += '0' * abs(len(bin_a) - len(bin_b))
            return bitwise_and(bin_a, bin_b)


def xor(bin_a, bin_b):  # исключающее ИЛИ (^)
    res = ''
    if len(bin_a) == len(bin_b):
        for i in range(len(bin_a)):
            if (bin_a[i] == '0' and bin_b[i] == '0') or (bin_a[i] == '1' and bin_b[i] == '1'):
                res += '0'
            else:
                res += '1'
        return res
    else:
        if len(bin_a) > len(bin_b):
            bin_b += '0' * abs(len(bin_a) - len(bin_b))
            return xor(bin_a, bin_b)
        else:
            bin_a += '0' * abs(len(bin_a) - len(bin_b))
            return xor(bin_a, bin_b)


def bitwise_not(bin_a):  # побитовое отрицание
    res = ''
    for i in bin_a:
        if i == '1':
            res += '0'
        else:
            res += '1'
    return res


def bit_shift_left(i, num):
    num = num[i:] + '0' * i
    return num


def bit_shift_right(i, num):
    if num[0] == '1':
        num = '1' * i + num[:len(num)-i]
    else:
        num = '0' * i + num[:len(num) - i]
    return num


bin_five = to_binary(5)
bin_six = to_binary(6)
print('5 | 6 = ', bitwise_or(bin_five, bin_six))
print('5 & 6 = ', bitwise_and(bin_five, bin_six))
print('5 ^ 6 = ', xor(bin_five, bin_six))
print('~5 =', bitwise_not(bin_five), ' ~6 =', bitwise_not(bin_six))
print(bit_shift_left(2, bin_five))
print(bit_shift_right(2, bin_five))
