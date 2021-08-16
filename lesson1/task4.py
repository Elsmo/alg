import random


def generate_random_values(user_text):
    if user_text == 'целое число':
        random_digit = [int(input('Укажите нижнюю границу: ')), int(input('Укажите верхнюю границу: '))]
        return random.randint(random_digit[0], random_digit[1])

    elif user_text == 'вещественное число':
        random_digit = [float(input('Укажите нижнюю границу: ')), float(input('Укажите верхнюю границу: '))]
        return round(random.uniform(random_digit[0], random_digit[1]), 2)

    elif user_text == 'символ':
        random_elem = [input('Укажите нижнюю границу: '), input('Укажите верхнюю границу: ')]
        return chr(random.randint((ord(random_elem[0])), ord(random_elem[1])))

    else:
        user_text = input('Вам нужно ввести один из предложенных вариантов: ')
        return generate_random_values(user_text)


user = input('Введите, что вы хотите сгенирировать: целое число, вещественное число, символ: ')
print(generate_random_values(user))
