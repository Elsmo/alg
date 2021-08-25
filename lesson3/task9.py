matrix = [[1, 2, 3, 4, 10], [5, 4, 2, 0, 12], [3, 2, 4, 6, 15], [7, 4, 5, 2, 18]]

matrix_min = matrix[0][0]
maximum_matrix_min = matrix[0][0]
for column in range(len(matrix)):
    for row in range(len(matrix[0])):
        if matrix[column][row] < matrix_min:
            matrix_min = matrix[column][row]
    if matrix_min > maximum_matrix_min:
        maximum_matrix_min = matrix_min
print(f'Максимальный среди минимальных: {maximum_matrix_min}')
