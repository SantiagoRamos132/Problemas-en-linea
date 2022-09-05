"""
Beecrowd
Problema 1044 Múltiplos
Link:https://www.beecrowd.com.br/judge/es/problems/view/1044
Se leen dos numeros y se usa una condicional para ver si el numero mayor es divisible entre el menor,
esto ocurre si el residuo de la division del mayor con el menor es 0.
"""
a,b = map(int,input().split())
if (a%b==0) or (b%a==0):
    print ("Sao Multiplos")
else:
    print("Nao sao Multiplos")