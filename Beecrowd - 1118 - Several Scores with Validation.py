"""
Beecrowd
Problema 1118 Several Scores with Validation
Link:https://www.beecrowd.com.br/judge/es/problems/view/1118
Se leen flotantes de entrada hasta que dos de ellos sean válidos (que se encuentren en el intervalo de [0,10]). Por cada flotante 
válido leído, se suma su valor a la variable de "SumaNotasValidas". Si un flotante es inválido, se imprime un mensaje indicándolo.
Una vez leídos dos flotantes válidos, se imprime el promedio de estos dos flotantes y se le pide al usuario un número que indica
si desea continuar (1 si desea, 2 si no). En caso de que el número digitado sea menor a 1 o mayor a 2, se vuelve a pedir este número.
Si el número digitado fue 1, se repite el programa desde el inicio. Si el número digitado fue 2, se termina el programa.
"""
X = 0
while (X!=2):
    SumaNotasValidas = 0
    NotasValidas = 0
    while (NotasValidas <2):
        Entrada = float(input())
        if (Entrada >=0 and Entrada <=10): #Entrada valida
            NotasValidas+=1
            SumaNotasValidas+=Entrada
        else:
            print("nota invalida")
    promedio = SumaNotasValidas/2
    print(f"media = {promedio:.2f}")
    print("novo calculo (1-sim 2-nao)")
    X = int(input())
    while (X < 1 or X>2):
        print("novo calculo (1-sim 2-nao)")
        X = int(input())
