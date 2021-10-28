# -*- coding: utf-8 -*- 

print('Универсальный калькулятор по нахождению величин фигур (пишите числа пронумерованных вариантов ответа)')
task = str(input('Какую фигуру желаете выбрать? Квадат(1) или прямоугольник(2)? '))

if task == '2' :
	task = str(input('Желаете найти площадь(1) или периметр(2) прямоугольника? '))
	if task == "2" :
		height = input('Высота: ')
		wight = input('Ширина: ')
		P = 2*(height + wight)
		P = str(P)
		print("Периметр равен: " + P)
	elif task == "1" :
		height = input('Высота: ')
		wight = input('Ширина: ')
		S = height * wight
		S = str(S)
		print("Площадь равна: " + S)

elif task == '1' :
	task = str(input('Желаете найти площадь(1) или периметр(2) квадрата? '))
	if task == "2" :
		a = input('Длина одной стороны: ')
		P = 4*a
		P = str(P)
		print("Периметр равен: " + P)
	elif task == "1" :
		a = input('Длина одной стоны: ')
		S = a * a
		S = str(S)
		print("Площадь равна: " + S)
