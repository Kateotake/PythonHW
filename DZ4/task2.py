# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))
lst = []
for i in range(2, n+1):
    while n % i == 0:
        n = n/i
        lst.append(i)
print(lst)    