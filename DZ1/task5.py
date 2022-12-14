# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координату точки А: ')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
print('Введите координату точки B: ')
x2 = int(input('x2: '))
y2 = int(input('y2: '))

S = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
S = round(S,2)
print(f'Расстояние между точками A({x1};{y1}) и B({x2};{y2}) равно {S}')