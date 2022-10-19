# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число N: '))
lst = []
i = 0
while i < n:
    i += 1
    p = (1+(1/i))**i
    lst.append(round(p,2))

print(lst)