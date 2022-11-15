"""
Beecrowd
Problema 2808 Caballos Otra Vez
Link:https://www.beecrowd.com.br/judge/es/problems/view/2808
Se crea una lista con los posibles movimientos del caballo en una casilla, luego se busca si la posición actual aplicada
en alguno de esos movimientos es la posición buscada, si sí, se imprime "VALIDO", si no, se imprime "INVALIDO".
"""
l = ["a","b","c","d","e","f","g","h"]
uno,dos = input().split()
def devuelveposennumero(string):
	x = int(string[1])
	i = 0
	while l[i] != string[0]:
		i+=1
	return [x,i+1]

mov = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
x = 0
posicion = devuelveposennumero(uno)
buscado = devuelveposennumero(dos)

for movimiento in mov:
	if [posicion[0]+movimiento[0],posicion[1]+movimiento[1]] == buscado:
		x = 1
if not x:
	print("INVALIDO")
else:
	print("VALIDO")