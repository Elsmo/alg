from collections import namedtuple
from statistics import mean


Company = namedtuple('Company', 'name profit avg')

res = []
user_text = int(input('Введите количество компаний: '))
for i in range(user_text):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел: ').split()
    res.append(Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in res])

for i in res:
    print(f'В {i.name} средняя прибыль за год: {i.avg}')

for i in res:
    if i.avg < avg:
        print(f'Прибыль меньше средней: {i.name}')

for i in res:
    if i.avg > avg:
        print(f'Прибыль больше средней: {i.name}')
