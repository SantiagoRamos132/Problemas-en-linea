"""
Beecrowd
Problema 2717 Elf Time
Link:https://www.beecrowd.com.br/judge/es/problems/view/2717
Dados los minutos restantes del día, si la cantidad de minutos que toma manufacturar los dos productos restantes es mayor al tiempo disponible, se 
imprime que no se pueden terminar de manufacturar ese mismo día. En caso contrario se imprime que si se pueden terminar de manufacturar ese mismo día.
"""
n = int(input())
a,b = map(int,input().split())
if a+b<=n:print("Farei hoje!")
else:print("Deixa para amanha!")
