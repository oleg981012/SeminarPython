# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите кординаты х1: '))
y1 = int(input('Введите кординаты y1: '))
x2 = int(input('Введите кординаты х2: '))
y2 = int(input('Введите кординаты y2: '))
import math
sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
print(f'Расстояние: (A - ({x1}, {y1}) между B - ({x2}, {y2}) = {sqrt}')