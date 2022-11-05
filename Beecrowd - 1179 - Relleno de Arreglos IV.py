"""
Beecrowd
Problema 1179 Relleno de Arreglos IV
Link:https://www.beecrowd.com.br/judge/es/problems/view/1179
Se crea una lista para números impares y otra lista para números pares, se leen 15 números, cada número es añadido
a una de las dos listas según su paridad. En el momento en que se añadan 5 elementos a alguna de las listas. Se imprime
la lista con el formato dado en el problema y se le eliminan todos los elementos.
"""
Limpar = []
Lpar = []
for _ in range(15):
    x = int(input())
    if x%2:
        Limpar.append(x)
        if len(Limpar)==5:
            for i in range(5):
                print(f"impar[{i}] = {Limpar[i]}")
            Limpar = []
    else:
        Lpar.append(x)
        if len(Lpar) == 5:
            for i in range(5):
                print(f"par[{i}] = {Lpar[i]}")
            Lpar = []
    if _ == 14:
        for i in range(len(Limpar)):
            print(f"impar[{i}] = {Limpar[i]}")
        for i in range(len(Lpar)):
            print(f"par[{i}] = {Lpar[i]}")
