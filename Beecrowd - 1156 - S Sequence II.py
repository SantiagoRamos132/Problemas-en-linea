"""
Beecrowd
Problema 1156 S Sequence II
Link:https://www.beecrowd.com.br/judge/es/problems/view/1156
Se crea una función recursiva representando a la Suma desde i=0 hasta n de (1+2*n)/2^i, y luego se imprime el resultado de la función cuando n es 19.
"""
def Suma(n):
    if n==-1:
        return 0
    return (1+2*n)/(2)**n + Suma(n-1)

print("%.2f"%Suma(19))
