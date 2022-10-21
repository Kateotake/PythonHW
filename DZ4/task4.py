# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

st = ''
k = int(input('Введите степень многочлена: '))

while k > -1:
    a = random.randint (0,100)
    if a != 0:
        if k == 0:
            st = st + f'+ {a} '
        elif k == 1:
            st = st + f'+ {a}*x '
        else:
            st = st + f'+ {a}*x^{k} '
    k -= 1
st = st + '= 0'
st = st[2:]
st = st.replace('1*x','x')
print(st)

with open("hello.txt", "w") as file:
    file.write(st)
