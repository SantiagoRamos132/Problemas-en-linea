"""
Beecrowd
Problema 2157 Secuencia Espejo
Link:https://www.beecrowd.com.br/judge/es/problems/view/2157
La idea es primero crear un string con los números de E hasta B, que sería la mitad de la secuencia, y luego concatenar el reverso de los números
desde B hasta E, para hacer esto se pasa cada número a string, se usa una función que devuelve este string invertido, y se concatena al string de la 
secuencia. 
"""
def Invertir_Str(string):
    resp = ""
    for char in string:
        resp = char+resp
    return resp 

C = int(input())
for _ in range(C):
    E,B = map(int,input().split())
    espejo = ""
    for numero in range(E,B+1): #incluir B
        espejo+=str(numero)
    for i in range(B-E+1): 
        numero = B-i
        espejo+=Invertir_Str(str(numero))
    print(espejo)