matrix_array = []
for i in range(4):
    string_array = []
    string_sum = 0
    for j in range(4):
        num = int(input(f'Введите {j+1} элемент {i+1} строки: '))
        string_sum += num
        string_array.append(num)
    string_array.append(string_sum)
    matrix_array.append(string_array)

for i in matrix_array:
    for j in i:
        print(j, end=' | ')
    print()
