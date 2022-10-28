"""
Beecrowd
Problema 1101 Secuencia de Números y Suma
Link:https://www.beecrowd.com.br/judge/es/problems/view/1101
Se leen dos números m y n, se itera desde el número menor al mayor, por cada número iterado, se agrega al string "texto"
y se suma a la variable "suma". Una vez finalizada la iteración, se imprime el string "texto", que contiene los números 
iterados y la variable "suma" que tiene la suma de los números iterados. El programa se detiene cuando alguno de los números
leídos es menor o igual a 0. (m<=0 or n<=0), lo que significa que el programa va a correrse cuando no ocurra que 
(m<=0 or n<=0), es decir, cuando la negación de la expresión (m<=0 or n<=0) sea verdadera. Usando ley de Morgan, se
obtiene que la negación de (m<=0 or n<=0) anterior es (m>0 and n>0). Por lo que se introduce tal cuál en el while
que corre el programa.
"""
m,n = map(int,input().split())
while (m > 0 and n>0):
    suma = 0
    texto = ""
    if m > n:
        for i in range (n,m+1):
            suma+=i
            texto+= f"{i} " 
        print(f"{texto}Sum={suma}")
    else:
        for i in range (m,n+1):
            suma+=i
            texto+= f"{i} " 
        print(f"{texto}Sum={suma}")
    m,n = map(int,input().split())