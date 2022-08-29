"""
Beecrowd
Problema 1010 Cálculo Simple
Link:https://www.beecrowd.com.br/judge/es/problems/view/1010
Se leen dos lineas que contienen el número de un producto, la cantidad a comprar y el precio del producto.
Se imprime la cantidad del primero producto por su precio + la cantidad del segundo producto por su precio.
Para obtener la cantidad de un producto y su precio se crea una lista separando la entrada que se guardo como string por sus espacios y seleccionando el segundo y tercer elemento de esa lista.
"""
A = input()
B = input()
a = A.split()
b = B.split()
p1 = float(a[1])*float(a[2])
p2 = float(b[1])*float(b[2])
print('VALOR A PAGAR: R$',format((p1 + p2 ),'.2f'))
