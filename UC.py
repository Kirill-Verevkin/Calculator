# -*- coding: utf-8 -*- 

print('Универсальный калькулятор по нахождению величин фигур (пишите числа пронумерованных вариантов ответа)')
task = str(input('Какую фигуру желаете выбрать? Квадат(1), прямоугольник(2) или треугольник(3)? '))


if task == '1' :
	task = str(input('Желаете найти площадь(1) или периметр(2) квадрата? '))
	if task == "1" :
		a = input('Длина одной стоны: ')
		S = a * a
		S = str(S)
		print("Площадь равна: " + S)
	elif task == "2" :
		a = input('Длина одной стороны: ')
		P = 4*a
		P = str(P)
		print("Периметр равен: " + P)


elif task == '2' :
	task = str(input('Желаете найти площадь(1) или периметр(2) прямоугольника? '))
	if task == "1" :
		height = input('Высота: ')
		wight = input('Ширина: ')
		S = height * wight
		S = str(S)
		print("Площадь равна: " + S)
	elif task == "2" :
		height = input('Высота: ')
		wight = input('Ширина: ')
		P = 2*(height + wight)
		P = str(P)
		print("Периметр равен: " + P)

elif task == '3' :
	task = str(input('Желаете найти площадь(1) или периметр(2) треугольника? '))
	if task == '1' :
		height = input('Высота: ')
		footing = input('Основание: ')
		S = (height * footing) / 2
		S = str(S)
		print('Площадь равна:' + S)
	elif task == '2' :
		side1 = input('Первая сторона: ')
		side2 = input('Вторая сторона: ')
		side3 = input('Третья сторона: ')
		P = side1 + side2 + side3
		P = str(P)
		print("Периметр равен: " + P)
