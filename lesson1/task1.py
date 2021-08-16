x = input('Введите трёхзначное число: ')
sum_x = 0
product_x = 1
for i in x:
    sum_x += int(i)
    product_x = product_x * int(i)
print(f'Сумма цифр: {sum_x} \nПроизведение цифр: {product_x}')
