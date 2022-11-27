"""
Beecrowd
Problema 1632 Variations
Link:https://www.beecrowd.com.br/judge/es/problems/view/1632
La idea es guardar cada contraseña como string, recorrer este string, de manera que si se encuentra un carácter especial (los que se pueden escribir
de 3 maneras distintas, en minúscula, mayúscula o en número), se multiplique por 3 la cantidad de variaciones de la contraseña, y sino, multiplicar por 2 esta cantidad de variaciones, ya que las únicas dos variaciones de este carácter son en mayúscula o en minúscula.
"""
charEspeciales = ['A','E','I','O','S','a','e','i','o','s']
T = int(input())
for _ in range(T):
    contra = input()
    variaciones = 1
    for char in contra:
        if char in charEspeciales:
            variaciones*=3 #Tienen 3 variaciones, 2 con mayuscula y minuscula, 1 con numero
        else:
            variaciones*=2
    print(variaciones)
