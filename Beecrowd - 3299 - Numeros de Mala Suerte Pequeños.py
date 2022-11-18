"""
Beecrowd
Problema 3299 Números de Mala Suerte Pequeños
Link:https://www.beecrowd.com.br/judge/es/problems/view/3299
La idea es recorrer el número de derecha a izquierda buscando si el digito menos significativo es un 3 y el segundo
dígito menos significativo es un 1, si esto se cumple, se imprime que el número es de mala suerte y se acaba el programa,
mientras esto no se cumpla, se divide el número entre 10 y se repite el proceso. Si el número luego de ser divido varias veces
termina siendo 0, se imprime que el número no es de mala suerte.
"""
n = int(input())
x = n
while n>0:
    if n%10==3 and (n//10)%10==1:
        print(x,"es de Mala Suerte")
        quit()
    n//=10
print(x,"NO es de Mala Suerte")
