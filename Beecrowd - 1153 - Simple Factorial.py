"""
Beecrowd
Problema 1153 Simple Factorial
Link:https://www.beecrowd.com.br/judge/es/problems/view/1153
Se crea la función recursiva de factorial a partir de la función matemática, y se imprime el factorial del número de la entrada.
"""
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
N = int(input())
print(fact(N))
