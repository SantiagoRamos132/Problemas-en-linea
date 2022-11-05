"""
Beecrowd
Problema 1175 Array change I
Link:https://www.beecrowd.com.br/judge/es/problems/view/1175
Se leen 20 números, cada vez que se lee un número se agrega a la primera posición de una lista, luego se imprime la lista empezando
por el primer elemento y terminando hasta el último utilizando el formato solicitado. 
De esta manera se imprime un arreglo empezando por el último elemento leído hasta terminarcon el primer elemento leído
"""
lista = []
for turnos in range(20):
    entero = int(input())
    lista.insert(0,entero)

for i in range(20):
    print(f"N[{i}] = {lista[i]}")
