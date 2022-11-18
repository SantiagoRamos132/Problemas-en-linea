"""
Beecrowd
Problema 3171 String Led
Link:https://www.beecrowd.com.br/judge/es/problems/view/3171
La idea es guardar las entradas en una lista de adyacencia, donde el elemento en la posición i-1 corresponde
a una lista con las conexiones del segmento i, luego usar una pila para recorrer esta lista de adyacencia,
marcando en una lista de números visitados los segmentos que se han visitado (que se encuentran adentro de los elementos
de un segmento de la lista de adyacencia). Una vez que se termina de usar la pila, se recorre la lista con los elementos visitados,
si algún elemento no fue marcado como visitado, se imprime "INCOMPLETO", en caso contrario, "COMPLETO".
"""
segmentos,conecciones = map(int,input().split())
la = [[] for i in range(segmentos)]

for _ in range(conecciones):
    a,b = map(int,input().split())
    la[a-1].append(b-1)
    la[b-1].append(a-1)

def copiarlista(l):
    r = []
    for i in l:
        r.append(i)
    return r

pila = [0]
visitados = [False for i in la]
visitados[0] = True
while pila!=[]:
    actual = pila.pop()
    for vecino in la[actual]:
        if not (visitados[vecino]):
            pila.append(vecino)
            visitados[vecino] = True
for b in visitados:
    if not b:
        print("INCOMPLETO")
        quit()
print("COMPLETO")
