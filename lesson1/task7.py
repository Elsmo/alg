x, y, z = int(input('Отрезок 1: ')), int(input('Отрезок 2: ')), int(input('Отрезок 3: '))
if x + y > z and x + z > y and y + z > x:
    print('треугольник существует')
    if x == y != z or y == z != x:
        print('треугольник равнобедренный')
    elif x != y != z:
        print('треугольник разносторонний')
    else:
        print('треугольник равносторонний')
else:
    print('треугольника не существует')
