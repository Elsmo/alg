def substrings(s):
    n = len(s)
    arr_str = set()
    for i in range(1, n):

        for j in range(n - i + 1):

            k = hash(s[j:j+i])

            if k not in arr_str:
                arr_str.add(k)

    return len(arr_str)


some_string = input('Введите строку: ')
print(f'Количество подстрок в вашей строке: {substrings(some_string)}')
