"""
Beecrowd
Problema 1155 S Sequence
Link:https://www.beecrowd.com.br/judge/es/problems/view/1155
Se crea una función recursiva representando a la Suma desde i=0 hasta n de 1/i, y luego se imprime el resultado de la función cuando n es 100.
"""
def Suma(n):
    if n<1:
        return 0
    return 1/n + Suma(n-1)
print("%.2f"%Suma(100))
