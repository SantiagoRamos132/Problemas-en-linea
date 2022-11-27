"""
Beecrowd
Problema 1943 Top N
Link:https://www.beecrowd.com.br/judge/es/problems/view/1943
La idea es guardar los top's en una lista, de manera que dada una entrada, se itere en los elementos de esta lista, donde si un top de la lista
es igual a la entrada, se imprima ese top, o si la entrada es mayor al top i de la lista y menor al top i+1 de la lista, se imprima que pertenece
al top i+1.
"""
tops = [1,3,5,10,25,50,100] 
k =  int(input())
encontrado = False
i = 0
while (not(encontrado)):
    if (tops[i]==k): #si es igual a un elemento del top
        encontrado=True
    else: #no es igual
        if (k > tops[i] and k < tops[i+1]):
            encontrado = True
        i+=1
print("Top",tops[i])