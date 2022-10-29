"""
Beecrowd
Problema 1117 Score Validation
Link:https://www.beecrowd.com.br/judge/es/problems/view/1117
Se leen flotantes de entrada hasta que dos de ellos sean válidos (que se encuentren en el intervalo [0,10]). Por cada flotante 
válido leído, se suma su valor a la variable de "SumaNotasValidas". Si un flotante es inválido, se imprime un mensaje indicándolo.
Una vez leídos dos flotantes válidos, se imprime el promedio.
"""
NotasValidas = 0
SumaNotasValidas = 0
while (NotasValidas <2):
    Entrada = float(input())
    if (Entrada >=0 and Entrada <=10): #Entrada valida
        NotasValidas+=1
        SumaNotasValidas+=Entrada
    else:
        print("nota invalida")
promedio = SumaNotasValidas/NotasValidas
print(f"media = {promedio:.2f}")
