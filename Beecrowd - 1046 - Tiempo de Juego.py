"""
Beecrowd
Problema 1046 Tiempo de Juego
Link:https://www.beecrowd.com.br/judge/es/problems/view/1046
Se reciben las horas de inicio y final. Debido a que el tiempo maximo que pueden transcurrir son 24 horas,
ocurren los siguientes tres casos:
-Si la hora inicial es menor a la final. El juego inicio y termino en el mismo dia. Por lo que se resta
el tiempo final con el tiempo inicial.
-Si la hora inicial es igual a la final. El tiempo transcurrido fue de 24 horas.
-Si la hora inicial es mayor a la final. El juego empezo un dia y acabo en el dia siguiente.
Para este caso, se le suma 24 horas al tiempo final (esto para 
obtener el tiempo transcurrido desde el primer dia), y se le resta el tiempo inicial.
"""
import math
i,f = map(int,input().split())
if i>=f:
    print(f"O JOGO DUROU {(f+24)-i} HORA(S)")
else:
    print(f"O JOGO DUROU {f-i} HORA(S)")