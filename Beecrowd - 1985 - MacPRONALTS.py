"""
Beecrowd
Problema 1985 MacPRONALTS
Link:https://www.beecrowd.com.br/judge/es/problems/view/1985
Se guarda la lista de precios en una lista, y por cada producto pedido, se suma a una variable del precio a 
pagar el valor del producto pedido que está guardado en la lista por la cantidad de veces que se va
a comprar este producto.
"""
l = [1.50,2.50,3.50,4.50,5.50]
x = int(input())
s = 0
for _ in range(x):
    num,cant = map(int,input().split())
    s+=l[num-1001]*cant
print(f"{s:.2f}")