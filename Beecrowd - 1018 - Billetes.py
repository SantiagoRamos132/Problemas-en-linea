"""

Beecrowd
Problema 1018 Billetes
Link: https://www.beecrowd.com.br/judge/es/problems/view/1018
Autor: Neilor Tonin
La solucion propuesta lee un entero n, luego utilizando un for se itera en una lista de enteros representando los billetes en que se puede descomponer n, 
ordenados de mayor a menor. 
Por cada entero "i" que se itera en la lista, se imprime la maxima cantidad de billetes de "i" valor en los que se puede descomponer n (n division entera entre i),
el valor de n pasa a ser el residuo de n dividido por i, y se itera al siguiente elemento de la lista.

"""

n = int(input())
print(n)
for i in [100,50,20,10,5,2,1]:
    print (f"{n//i} nota(s) de R$ {i},00")
    n = n%i
