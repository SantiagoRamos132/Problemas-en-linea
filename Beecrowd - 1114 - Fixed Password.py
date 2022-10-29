"""
Beecrowd
Problema 1114 Fixed Password
Link:https://www.beecrowd.com.br/judge/es/problems/view/1114
Se lee un entero correspondiente a una contraseña, y mientras esa contraseña no sea 2002, se imprime que la contraseña digitada es inválida y se repite
el proceso hasta que la contraseña ingresada sea 2002. Cuando la contraseña ingresada sea 2002, se imprime "Acesso Permitido" y se termina el programa.
"""
numero = int(input())
while (numero!=2002):
    print("Senha Invalida")
    numero = int(input())
print("Acesso Permitido")
