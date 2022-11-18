"""
Beecrowd
Problema 1168 LED
Link:https://www.beecrowd.com.br/judge/es/problems/view/1168
Se crea una lista con la cantidad de leds que se necesita para cada número, donde el primer elemento de la lista corresponde a
la cantidad de leds para el numero 1, el segundo elemento corresponde a la cantidad de leds para el número 2 etc.
Luego se recorre el número leído como un string y por cada carácter leído se suma la cantidad de leds
necesarios para formar ese número a una variable de respuesta.
"""
l = [2,5,5,4,5,6,3,7,6,6]
for _ in range(int(input())):
	a = input()
	resp = 0
	for num in a:
		resp+=l[int(num)-1]
	print(resp,"leds")
