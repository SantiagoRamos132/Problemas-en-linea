"""
Beecrowd
Problema 1049 Animal
Link:https://www.beecrowd.com.br/judge/es/problems/view/1049
La solución al problema es recorrer la tabla comparando los datos del animal con cada caracteristica posible de la tabla
para obtener imprimir el nombre del animal dado.
La busqueda se empieza de la izquierda a la derecha de la tabla para evitar comparaciones innecesarias (por ejemplo,
si el animal es vertebrado, no se necesita recorrer la lista de invertebrados ya que no lo es).
"""
a = input()
b = input()
c = input()
if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro": print("aguia")
        else: print("pomba")
    else:
        if c == "onivoro": print("homem")
        else: print("vaca")

if a == "invertebrado":
    if b == "inseto":
        if c == "hematofago": print("pulga")
        else: print("lagarta")
    else:
        if c == "hematofago": print("sanguessuga")
        else: print("minhoca")
