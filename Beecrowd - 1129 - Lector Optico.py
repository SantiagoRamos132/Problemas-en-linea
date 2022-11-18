"""
Beecrowd
Problema 1129 Lector Óptico
Link:https://www.beecrowd.com.br/judge/es/problems/view/1129
La idea es guardar las respuestas en una lista, recorrer la lista e ir sumando a una variable la cantidad de respuestas
marcadas en negro y a otra variable la última respuesta marcada en negro. Si la cantidad de respuestas marcadas en negro
es diferente de 1, se  imprime que la pregunta es anulada, sino, se imprime cuál fue la respuesta marcada por el estudiante usando
la variable de la respuesta marcada como negra.
"""
while True:
    preguntas = int(input())
    if preguntas==0:break
    for _ in range(preguntas):
        A,B,C,D,E = map(int,input().split())
        negras = 0
        resp = 0
        l = [A,B,C,D,E]
        l2 = ["A","B","C","D","E"]
        for i in range(5):
            if l[i]<=127:
                negras+=1
                resp = i
        if negras!=1:
            print("*")
        else:
            print(l2[resp])
