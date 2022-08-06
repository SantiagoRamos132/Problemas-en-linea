"""

Beecrowd
Problema 1038 Snack
Enlace: https://www.beecrowd.com.br/judge/es/problems/view/1038
Adaptado por Neilor Tonin
Solucion: Se crea una lista "precio" de flotantes que representan los precios de cada producto ordenados por el numero de codigo de menor a mayor.
Luego se leen dos enteros "x" y "y", donde "x" es el codigo del producto y "y" la cantidad de ese producto a comprar.
Finalmente se imprime el precio total a pagar, que es el producto de "y" por el flotante en la posicion "x"-1 de la lista de precios (esto debido a que el 
precio del producto 1 se encuentra en la posicion 0 de la lista, el precio del producto 2 en la posicion 1 de la lista y asi sucesivamente).

"""

x,y = list(map(int,(input().split())))
precio = [4.00,4.50,5.00,2.00,1.50]
paga = precio[x-1]*y
print(f'Total: R$ {paga}0')
