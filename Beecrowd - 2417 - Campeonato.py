"""
Beecrowd
Problema 2417 Campeonato
Link:https://www.beecrowd.com.br/judge/es/problems/view/2417
Primero se obtienen los puntos de ambos equipos multiplicando el número de victorias por 3 y sumando la cantidad de empates,
si algún equipo tiene más puntos que el otro, se imprime la primera letra correspondiente a este equipo, en caso de que 
tengan la misma cantida de puntos, se compara el número de goles de ambos y se imprime la letra del equipo con más goles,
y si tienen la misma cantidad de goles, se imprime el carácter '=' que significa que hubo empate.
"""
cv,ce,cg,fv,fe,fg = map(int,input().split())
puntosc = cv*3+ce
puntosf = fv*3+fe
if puntosc > puntosf:
    print("C")
    quit()
if puntosc < puntosf:
    print("F")
    quit()
#Numeros de puntos iguales
if cg > fg:
    print("C")
    quit()
elif cg < fg:
    print("F")
    quit()
else:
    print("=")