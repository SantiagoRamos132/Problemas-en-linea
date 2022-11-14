"""
Beecrowd
Problema 2708 Turistas en el Parque Huacachina
Link:https://www.beecrowd.com.br/judge/es/problems/view/2708
Se crean dos variables T y J, donde T corresponde al número de jeeps y J al número de turistas que aún no han regresado
al parque. Por cada entrada, si el primer string corresponde a "SALIDA", se agrega 1 a J, y la cantidad de turistas saliendo
a T, sino, se resta 1 a J y la cantidad de turistas regresando a T.
"""
t = 0
j = 0
while True:
	x = input()
	if x == "ABEND": break
	a,b = x.split()
	b = int(b)
	if a == "SALIDA":
		j+=1
		t+=b
	if a == "VUELTA":
		j-=1
		t-=b
print(t)
print(j)
