"""
Beecrowd
Problema 2497 Counting Cycles
Link:https://www.beecrowd.com.br/judge/es/problems/view/2497
La idea es ver que por cada dos pasos se obtiene un ciclo, entonces si se tienen N pasos, se tienen N (división entera) entre dos ciclos. Entonces
por cada entrada, se imprime el número del experimento leído, se obtienen los ciclos del experimento dividiendo enteramente los pasos entre 2 y
se imprime la cantidad de ciclos obtenida.
"""
pasos = int(input())
experimentos =1
while (pasos != -1):
    ciclos = pasos//2
    print(f"Experiment {experimentos}: {ciclos} full cycle(s)")
    pasos = int(input())
    experimentos+=1
