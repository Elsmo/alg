from operator import itemgetter


def sum_in_num(num):
    sum_num = 0
    for i in num:
        sum_num += int(i)
    return sum_num


user = ''
biggest = []
while user != '0':
    user = input('Введите число: ')
    if user == '0':
        biggest = sorted(biggest, key=itemgetter(1))
        print(f'Число с наибольшей суммой цифр: {biggest[-1][0]} \nCумма его цифр: {biggest[-1][1]}')
        break
    else:
        biggest.append((user, sum_in_num(user)))
