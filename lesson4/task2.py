import time


start_time = time.time()


def eratos(n):
    nums = list(range(2, n + 1))
    for num in nums:
        if num != 0:
            for i in range(2 * num, n + 1, num):
                nums[i - 2] = 0
    simple_nums = [j for j in nums if j != 0]
    return simple_nums


def prime(n):
    lst = []
    for i in range(2, n + 1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


user_num = int(input('Число, до которого хотим найти простые числа: '))
simple_index = int(input('Какое по счёту простое число вы бы хотели увидеть: '))
print(f'{eratos(user_num)[simple_index-1]}')  # 6.418184518814087 seconds
print(f'{prime(user_num)[simple_index-1]}')  # 2.824495553970337 seconds
print("--- %s seconds ---" % (time.time() - start_time))
