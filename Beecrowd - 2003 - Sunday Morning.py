"""
Beecrowd
Problema 2003 Sunday Morning
Link:https://www.beecrowd.com.br/judge/es/problems/view/2003
La idea de esta solución es tomar en cuenta que si Cino se levanta antes de las 7:00, no va a llegar tarde, sin embargo,
si esto no pasa, se obtiene el atraso máximo considerando que Cino se tardó 60min en llegar a la estación desde que se levantó.
"""
import sys
for line in sys.stdin:
    a,b = list(map(int,line.split(":")))
    if a>6:
        print(f"Atraso maximo: {b+(a%7)*60}")
    else:
        print(f"Atraso maximo: 0")
