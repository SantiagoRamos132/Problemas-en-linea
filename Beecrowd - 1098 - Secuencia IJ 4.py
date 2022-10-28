"""
Beecrowd
Problema 1098 Secuencia IJ 4
Link:https://www.beecrowd.com.br/judge/es/problems/view/1098
La idea es imprimir una secuencia que utiliza dos variables, "I" y "J".
En esta secuencia, se imprime el valor de I tres veces, acompañado primero por el valor de J, luego J+1 y por último J+2. Una vez que se imprimido esto, se 
le suma 0.2 a ambas variables y se repite hasta que I = 2.
Debido a que los numeros flotantes en las computadoras no son exactos. Se usa una variable de un entero que represente el número flotante de ambas variables. 
"""
I = -1
J = 0
cont = 0
decimales = 0
while cont!=3:
    decimales%=10
    if decimales == 0:
        I+=1
        J+=1
        print(f"I={I} J={J}")
        print(f"I={I} J={J+1}")
        print(f"I={I} J={J+2}")
        cont+=1
    else:
        print(f"I={I}.{decimales} J={J}.{decimales}")
        print(f"I={I}.{decimales} J={J+1}.{decimales}")
        print(f"I={I}.{decimales} J={J+2}.{decimales}")
    decimales+=2
