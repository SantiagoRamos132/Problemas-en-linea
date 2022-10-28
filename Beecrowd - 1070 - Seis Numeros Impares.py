"""
Beecrowd
Problema 1070 Seis Números Impares
Link:https://www.beecrowd.com.br/judge/es/problems/view/1070
Se lee la entrada y se imprimen 6 números impares consecutivos de esta entrada.
Para esto se le suma 1 a la entrada en caso de que sea par. Y se imprime cada número impar consecutivo a partir de esta entrada.
"""
X = int(input())
if X%2 == 0:
    X+=1
suma = 0
for i in range(6):
    print(X+suma)
    suma +=2
