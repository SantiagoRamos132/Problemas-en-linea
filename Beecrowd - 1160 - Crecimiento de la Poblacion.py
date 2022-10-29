"""
Beecrowd
Problema 1160 Crecimiento de la Población
Link:https://www.beecrowd.com.br/judge/es/problems/view/1160
Se simula el crecimiento año por año de ambas ciudades, guardando en una variable los años pasados y usando un bucle en el
cuál se actualiza la población de ambas ciudades según pasa cada año, y se termine cuando la población de la ciudad A sea mayor a la población
de la ciudad B, o pasen más de 100 años. Una vez terminado el bucle, si pasarón más de 100 años, se imprime que se necesita
más de un siglo para que la ciudad A tenga mayor población a la de la ciudad B. Y si no, se imprime cuantos años deben
pasar para que la población de la ciudad A sea mayor a la población de la ciudad B.
"""
T = int(input())
for _ in range(T):
    lista = input().split()
    PA,PB = map(int,lista[:2])
    CRA,CRB = map(float,lista[2:])
    anos = 0
    while PA<=PB and anos<101:
        PA = int((PA*(CRA+100)/100))
        PB = int(PB*(CRB+100)/100)
        anos+=1
    if anos==101:print("Mais de 1 seculo.")
    else:print(f"{anos} anos.")