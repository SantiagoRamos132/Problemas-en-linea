"""
Beecrowd
Problema 2958 The Bad Vibes Walk
Link:https://www.beecrowd.com.br/judge/es/problems/view/2958
La idea es guardar en listas distintas las entradas con problemas de vida y las entradas con problemas de disciplina,
luego ordenar las listas de mayor a menor y por último imprimir la lista de problemas de vida seguido de la lista
de problemas de disciplina.
"""
a,b = map(int,input().split())
life = []
discipline = []
for i in range(a):
    l = input().split()
    for elem in l:
        if elem[1] == "V":
            life.append(elem)
        else:
            discipline.append(elem)

discipline.sort(reverse=True)
life.sort(reverse=True)

if life!= []:
    for i in life:
        print(i)
if discipline!=[]:
    for i in discipline:
        print(i)