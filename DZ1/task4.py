# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


n = int(input('Введите номер четверти: '))

if n == 1:
    print(f'Диапазон координаты точки для {n}-й четверти - (x > 0 and y > 0)')
elif n == 2:
    print(f'Диапазон координаты точки для {n}-й четверти - (x > 0 and y < 0)')
elif n == 3:
    print(f'Диапазон координаты точки для {n}-й четверти - (x < 0 and y < 0)')
elif n == 4:
    print(f'Диапазон координаты точки для {n}-й четверти - (x < 0 and y > 0)')
else:
    print('Такой четверти нет')