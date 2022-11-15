"""
Beecrowd
Problema 2936 ¿Cuánto Locro?
Link:https://www.beecrowd.com.br/judge/es/problems/view/2936
Se lee la cantidad de porciones de locro de cada persona, y se multiplica cada una por el valor de una porción en gramos de la persona leída, y luego se suman
para obtener la cantidad total locro en gramos que Doña Juana debe preparar.
"""
a = int(input())
mart = int(input())
j = int(input())
mari = int(input())
i = int(input())
print (a*300+mart*1500+j*600+mari*1000+i*150+225)
