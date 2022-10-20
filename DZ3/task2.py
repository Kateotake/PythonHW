# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

def prod_el(lst):
    lst2 = []
    for i in range(math.ceil(len(lst)/2)):

        lst2.append(lst[i] * lst[-i-1])
        i +=1
    return lst2

num = list(map(int, input('Введите значения через пробел: ').split()))
print(num)
print(prod_el(num))
