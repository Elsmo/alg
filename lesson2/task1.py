def calculator(x, y, operation):
    if operation not in '+-/*':
        operation = input('Введите правильный оператор: ')
        return calculator(x, y, operation)
    else:
        if operation == '+':
            return f'{x}+{y}= {x+y}'
        elif operation == '-':
            return f'{x}-{y}= {x-y}'
        elif operation == '/':
            if b == '0':
                return 'Деление на ноль невозможно!'
            else:
                return f'{x}/{y}= {x//y}'
        elif operation == '*':
            return f'{x}*{y}= {x*y}'


a = ''
b = ''

while a != '0':
    a = int(input('Введите первое число: '))
    if a == 0:
        print('Good bye!')
        break
    else:
        b = int(input('Введите второе число: '))
        oper = input('Введите знак операции: ')
        print(calculator(a, b, oper))
