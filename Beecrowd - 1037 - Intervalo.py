"""
Beecrowd
Problema 1037 Intervalo
Link:https://www.beecrowd.com.br/judge/es/problems/view/1037
Se lee un flotante y se utilizan condicionales para encontrar en cual intervalo del enunciado del problema se encuentra.
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
