"""

Beecrowd
Problema 1037 Intervalo
Enlace: https://www.beecrowd.com.br/judge/es/problems/view/1037
Adaptado por Neilor Tonin.
Solucion: Se lee un numero flotante, se utiliza un if para ver si el numero esta fuera del rango de 0 a 100, en caso de estar,
se utilizan 4 ifs para ver en que rango se encuentra el flotante. Una vez encontrado el rango, se imprime.


"""


num = float(input())
if (num<0) or (num>100):
    print("Fora de intervalo")
elif (num >= 0) and (num <=25):
    print("Intervalo [0,25]")
elif num > 25 and num <= 50:
    print("Intervalo (25,50]")
elif num>50 and num<=75:
    print("Intervalo (50,75]")
elif num>75 and num<=100:
    print("Intervalo (75,100]")
