"""
Beecrowd
Problema 1009 Salario con Bonus
Link:https://www.beecrowd.com.br/judge/es/problems/view/1009
La idea del programa es leer el nombre del vendedor, su salario fijo y el total de ventas realizadas por él en el mes e imprimir su ganancia a fin de mes, que es el salario fijo + el 15% de las ventas realizadas.
"""
num = input()
sal = float(input())
ventas= float(input())
print(f"TOTAL = R$ {(sal+15/100*ventas):.2f}")
