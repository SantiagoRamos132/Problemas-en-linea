"""
Beecrowd
Problema 2630 Greyscale
Link:https://www.beecrowd.com.br/judge/es/problems/view/2630
La idea es guardar cada entrada en una lista de enteros, e imprimir el color de grís de ese pixel según la conversión pedida usando la lista anterior.
"""
t = int(input())
for _ in range(1,t+1):
    string = input()
    l = list(map(int,input().split()))
    if string == "min":
        print(f"Caso #{_}: {min(l)}")
    elif string == "max":
        print(f"Caso #{_}: {max(l)}")
    elif string == "eye":
        print(f"Caso #{_}: {int(0.30*l[0] + 0.59*l[1] + 0.11*l[2])}")
    else:
        print(f"Caso #{_}: {(l[0]+l[1]+l[2])//3}")
