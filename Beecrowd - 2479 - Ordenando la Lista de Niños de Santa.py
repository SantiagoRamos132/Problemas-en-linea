"""
Beecrowd
Problema 2479 Ordenando la Lista de Niños de Santa
Link:https://www.beecrowd.com.br/judge/es/problems/view/2479
La idea es que cada vez que se lea una entrada, se agrege el nombre del niño a la lista de nombres, y dependiendo del primer
carácter leido, se sume 1 a la variable de niños que se portaron bien o de niños que se portaron mal. Luego de leer las entradas,
se ordena la lista con los nombres de los niños, se imprime esta lista y la cantidad de niños que se portaron bien y la cantidad
de niños que se portaron mal.
"""
N = int(input())
lista = []
Bien = 0
mal = 0
for _ in range(N):
    a,b = input().split()
    lista.append(b)
    if a == "+":Bien+=1
    else:mal+=1
lista.sort()
for nino in lista:
    print(nino)
print(f"Se comportaram: {Bien} | Nao se comportaram: {mal}")