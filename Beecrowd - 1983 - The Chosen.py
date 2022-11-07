"""
Beecrowd
Problema 1983 The Chosen
Link:https://www.beecrowd.com.br/judge/es/problems/view/1983
La idea es recorrer las entradas, actualizando la variable de "mayornota" con el valor de la nota más grande leída hasta el momento y la variable "estudiante" con el nombre de el estudiante que obtuvo esta nota. Al leer una entrada, si la nota leída es  mayor a "mayornota" y es mayor o igual a 8, se actualiza "mayornota" y "estudiante" con los datos de esta entrada.
Si después de recorrer las entradas, no se actualizó "estudiante", se imprime que no se alcanzó la nota mínima, en caso contrario, se imprime el nombre del estudiante almacenado en esta variable.
"""
n = int(input())
mayornota = 0
estudiante = ""
for _ in range(n):
    l = input().split()
    a = l[0]
    b = float(l[1])
    if b>=8 and b>mayornota:
        mayornota = b
        estudiante = a
if estudiante == "":
    print("Minimum note not reached")
else:
    print(estudiante)
