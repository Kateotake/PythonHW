# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

with open('Sem/file.txt', 'r') as my_file:
    n = int(my_file.readline(2)) * int(my_file.readline(4))
print(n)