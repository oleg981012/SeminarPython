# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

x=int(input('Введите кординату x: '))
y=int(input('Введите кординату y: '))

if  x < 0 and y > 0:
    print("1я четверть")
elif x > 0 and y > 0:
    print("21я четверть")    
elif x < 0 and y < 0:
    print("3я четверть")    
elif x > 0 and y < 0:
    print("4я четверть")
else:
    print("Некорректный ввод")
