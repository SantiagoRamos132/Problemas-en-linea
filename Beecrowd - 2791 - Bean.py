"""
Beecrowd
Problema 2791 Bean
Link:https://www.beecrowd.com.br/judge/es/problems/view/2791
Se guardan los enteros en una lista, que se recorre hasta encontrar un 1, y se imprime la posición de entero +1, ya que en
las listas el elemento i está en la posición i-1,
"""
lista = list(map(int,input().split()))
for i in range(len(lista)):
    if lista[i] ==1:
        print (i+1)