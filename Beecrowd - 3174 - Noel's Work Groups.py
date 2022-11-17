"""
Beecrowd
Problema 3174 Noel's Work Groups
Link:https://www.beecrowd.com.br/judge/es/problems/view/3174
Se guarda en una lista con 4 elementos cúantos elfos hay para cada grupo (el primer elemento contiene el total de elfos para
el grupo de muñecos, el segundo elemento para arquitectos etc.), y luego se obtiene la cantidad de regalos que puede producir
cada grupo en un día y se suma estas cantidades para obtener el total de regalos producidos entre los 4 grupos en un día.
"""
n = int(input())
resp = 0
l = [0,0,0,0]
for _ in range(n):
    entrada = list(input().split())
    if entrada[1] == "bonecos":
        l[0]+= int(entrada[2])
    if entrada[1] == "arquitetos":
        l[1]+= int(entrada[2])
    if entrada[1] == "musicos":
        l[2]+= int(entrada[2])
    if entrada[1] == "desenhistas":
        l[3]+= int(entrada[2])

resp+=l[0]//8
resp+=l[1]//4
resp+=l[2]//6
resp+=l[3]//12
print(resp)
