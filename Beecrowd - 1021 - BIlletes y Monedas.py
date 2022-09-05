"""
Beecrowd
Problema 1021 Billetes y Monedas
Link:https://www.beecrowd.com.br/judge/es/problems/view/1021
Se lee el valor monetario y se almacena en una variable "x" la parte entera del valor y en otra variable "y" los digitos después
del punto decimal. Utilizando x, se calcula e imprime en cuantos billetes de 100,50,20,10,5 y 2 se puede descomponer el valor de x, para eso se utiliza el for que itera en una lista de los valores de los billetes y calcula la mínima cantidad de billetes en los que se pueden descomponer la variable de la parte entera.
Luego se aplica el mismo proceso con la variable "y" para calcular e imprimir la mínima cantidad de monedas en las que se puede descomponer dicha variable.
"""
x,y = map(int,input().split("."))

print("NOTAS:")
for i in [100,50,20,10,5,2]:
    print (f"{x//i} nota(s) de R$ {i}.00")
    x = x%i

print("MOEDAS:")
print(f"{x%2} moeda(s) de R$ 1.00")
for i in [50,25,10,5,1]:
    print (f"{y//i} moeda(s) de R$ {i/100:.2f}")
    y =y%i
