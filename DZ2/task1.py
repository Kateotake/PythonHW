# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите вещественное число: ')
m = list(n)  # преобразуем в список строк

for el in m:
    if el == '.':
        m.remove('.')
    elif el == ',':
        m.remove(',')

c = [int(i) for i in m] # преобразуем в список чисел

s = 0
for i in c:
    s += i
print(f'Сумма цифр равна {s}')