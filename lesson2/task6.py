import random

attempt = 10
random_num = random.randint(0, 100)
while attempt > 0:
    user_try = input('Какое число загаданно: ')
    if int(user_try) > random_num:
        attempt -= 1
        print('Это число больше загаданного')
    elif int(user_try) < random_num:
        print('Это число меньше загаданного')
        attempt -= 1
    else:
        print(f'Вы угадали! Это число: {random_num}')
        break
if attempt == 0:
    print(f'Попытки закончились :( Мы загадали {random_num}')
