"""
Beecrowd
Problema 1052 Mes
Link:https://www.beecrowd.com.br/judge/es/problems/view/1052
Se crea una lista con los nombres de los meses del año, se lee el número del mes del año a imprimir,
y se imprime el mes correspondiente(que es el elemento en la posición número del mes -1, ya que en una lista
en la posicion 0 se guarda el primer elemento, en la posición 1 el segundo y así sucesivamente)
"""
meses = ("January","February","March","April","May","June","July","August","September","October","November","December")
num = int(input())
print(meses[num-1])