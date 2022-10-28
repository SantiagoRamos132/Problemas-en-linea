"""
Beecrowd
Problema 1050 DDD
Link:https://www.beecrowd.com.br/judge/es/problems/view/1050
Se crea un diccionario que dado una llave(en este caso, un número), devuelve el nombre de la ciudad. Luego dado un número,
se verifica si este número pertenece a una llave del diccionario, si sí pertenece, se imprime su ciudad, si no, se imprime
que no esta registrado.
"""
a = int(input())
dic = {61:"Brasilia",71:"Salvador",11:"Sao Paulo", 21:"Rio de Janeiro",32:"Juiz de Fora",19:"Campinas",27:"Vitoria",31:"Belo Horizonte"}
if a in dic:
    print(dic[a])
else:
    print("DDD nao cadastrado")