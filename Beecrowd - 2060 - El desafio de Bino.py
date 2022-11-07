"""
Beecrowd
Problema 2060 El desafío de Bino
Link:https://www.beecrowd.com.br/judge/es/problems/view/2060
Por cada número leído, si el número es divisible entre 2,3,4 o 5 (el número leído al ser dividido entre
2,3,4 o 5 da residuo 0), se aumenta en 1 a una variable indicando la cantidad múltiplos de 2,3,4 o 5 leídos.
Luego se imprimen estas cantidades en el formato dado por el problema.
"""
N = int(input())
de2 = 0
de3 = 0
de4 = 0
de5 = 0
lista = list(map(int,input().split()))
for i in lista:
    if not i%2: de2+=1
    if not i%3: de3+=1
    if not i%4: de4+=1
    if not i%5: de5+=1
print(f"{de2} Multiplo(s) de 2")
print(f"{de3} Multiplo(s) de 3")
print(f"{de4} Multiplo(s) de 4")
print(f"{de5} Multiplo(s) de 5")