"""
Beecrowd
Problema 3039 Santa's Toys
Link:https://www.beecrowd.com.br/judge/es/problems/view/3039
Por cada entra leída, si el último carácter de la entrada es una F, se suma 1 a la cantidad de muñecas a hacer, sino, se suma 1 a la cantidad de carros
a hacer, luego de leer las entradas se imprime cuántos carros y muñecas debe hacer Santa.
"""
n = int(input())
ca = 0
bo = 0
for _ in range(n):
    string = input()
    if string[-1] == "F":
        bo+=1
    else:
        ca+=1

print(f"{ca} carrinhos\n{bo} bonecas")
