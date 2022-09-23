day = int(input('Введите число: ')) # соответствующее дню недели
if day > 7 or day < 1:
    print('Некорректное число')
elif day == 6 or day == 7:
    print("Это выходной день!")
else:
    print("Это будний день!")

