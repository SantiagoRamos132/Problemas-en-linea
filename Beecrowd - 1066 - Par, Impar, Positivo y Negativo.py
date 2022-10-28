"""
Beecrowd
Problema 1066 Par, Impar, Positivo y Negativo
Link:https://www.beecrowd.com.br/judge/es/problems/view/1066
Se leen 5 números y se suma 1 a las variables de números pares,impares,positivos y negativos 
según cada número leído y luego se imprimen. Si el número leído es cero, este no clasifica como negativo
o positivo, ya que es neutro (cualquier número sumado por 0 es el mismo).
"""
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(5):
    num = int(input())
    if num%2==0:
         pares+=1
    else:
        impares+=1
    if num > 0: positivos+=1
    elif num <0: negativos+=1

print(pares,"valor(es) par(es)")
print(impares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")