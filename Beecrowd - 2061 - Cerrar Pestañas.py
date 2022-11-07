"""
Beecrowd
Problema 2061 Cerrar Pestañas
Link:https://www.beecrowd.com.br/judge/es/problems/view/2061
Se leen las acciones realizadas por Péricles, si la acción corresponde a cerrar una ventana,
se aumenta el número de ventanas en 1 (ya que surgen dos nuevas pero se cierra una, entonces se termina
con una ventana extra), si hace click en un anuncio, se disminuye el número de ventanas en 1.
Luego se imprime el número final de pestañas.
"""
N,M = map(int,input().split())
for i in range(M):
	inp = input()
	if inp == "fechou":
		N+=1
	else:
		N-=1
print(N)