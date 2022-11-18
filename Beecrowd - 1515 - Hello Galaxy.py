"""
Beecrowd
Problema 1515 Hello Galaxy
Link:https://www.beecrowd.com.br/judge/es/problems/view/1515
La idea separar la información de las entradas en dos listas, la primera conteniendo el nombre de un planeta
y la segunda el año en que se envió, luego se busca el planeta que envió un mensaje en el año más pasado (el año
con el menor valor) y se imprime.
"""
while True:
    n = int(input())
    if n==0:quit()
    planetas = []
    anos = []
    for _ in range(n):
        entrada = input().split()
        ano = int(entrada[1])-int(entrada[2])
        planetas.append(entrada[0])
        anos.append(ano)
    anomenor = anos[0]
    planetaresp = planetas[0]
    for i in range(len(anos)):
        if anos[i] < anomenor:
            anomenor = anos[i]
            planetaresp= planetas[i]
    print(planetaresp)