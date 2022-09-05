"""
Beecrowd
Problema 1040 Promedio 3
Link:https://www.beecrowd.com.br/judge/es/problems/view/1040
Se leen las cuatro notas del examen y se calcula el promedio ponderado, que se obtiene con una proporción de los valores
ganados versus el total de valores posible. Luego según el valor del promedio se imprime si el alumno aprobó, reprobó o si puede hacer un exámen de reposición. En el último caso, se lee el valor de este examen y, se vuelve a calcular el promedio y se imprime si aprobó o reprobó.
"""
n1,n2,n3,n4 = map(float,input().split())
prom = (2*n1+3*n2+4*n3+n4)/10
print("Media: %.1f"%(prom))
if prom >= 7.0:
    print("Aluno aprovado.")
elif prom <5.0:
    print("Aluno reprovado.")
elif prom >=5.0 and prom <=6.9:
    print("Aluno em exame.")
    x = float(input())
    print ("Nota do exame:",x)
    prom2 = (prom+x)/2
    if prom2 >= 5.0:
        print("Aluno aprovado.")
    else: print("Aluno reprovado.")
    print("Media final:",prom2)
