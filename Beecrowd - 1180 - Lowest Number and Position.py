"""
Beecrowd
Problema 1180 Lowest Number and Position
Link:https://www.beecrowd.com.br/judge/es/problems/view/1180
Se leen N números y se guardan en una lista. Luego se recorre la lista buscando el número con el valor más pequeño
y su posición, para esto, se toma primero el primer número como el más pequeño, luego se empieza a recorrer la lista
de manera que cada vez que encuentre un número más pequeño al guardado anteriormente, actualize una variable correspondiente
al valor del número más pequeño visto actualmente y a la variable de su posición. Finalmente se imprimen el valor de estas
dos variables en el formato solicitado.
"""
N = int(input())
l = list(map(int,input().split()))
menor = l[0]
posicionmenor = 0
i = 0
while i < N:
    if l[i] < menor:
        posicionmenor = i
        menor = l[i]
    i+=1
print(f"Menor valor: {menor}\nPosicao: {posicionmenor}")
