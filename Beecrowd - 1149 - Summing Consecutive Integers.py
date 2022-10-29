"""
Beecrowd
Problema 1149 Summing Consecutive Integers
Link:https://www.beecrowd.com.br/judge/es/problems/view/1149
Se guardan los números de la entrada en una lista, se almacena en una variable el primer elemento de la lista, y se busca
en la lista de izquierda a derecha, un número mayor que 1, empezando desde el segundo elemento de la lista.
Una vez encontrado ese número, con la ayuda de la fórmula de Gauss, se obtiene la suma de los números
desde el primer elemento de la lista hasta ese segundo elemento encontrado.
"""
L = list(map(int,input().split()))
base = L[0]
posSig = 1
SigNumero = L[posSig]
while (SigNumero<1):
    posSig+=1 
    SigNumero = L[posSig]

def suma(a,b):
    return (((b*(b+1))//2) - (a*(a-1))//2)

print(suma(base,base+SigNumero-1))
