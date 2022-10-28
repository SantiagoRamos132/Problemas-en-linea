"""
Beecrowd
Problema 1094 Experimentos
Link:https://www.beecrowd.com.br/judge/es/problems/view/1094
Se crea una variable para cada animal la cuál guarda cuantos animales fueron usados, y otra variable del total de animales usados.
Luego, por cada caso de prueba se actualizan las variables anteriores según que animal fue usado. Después de leer los casos de pruebas, se imprime la cantidad 
de animales usados por cada tipo, y su procentaje frente al total de animales usados.
"""
n = int(input()) #Casos pruebas que van a ser input
c = 0
r = 0
s = 0
total = 0
for i in range(n):
    a,b = list(input().split())
    a = int(a)
    total+= a
    if b == "C": c+=a
    elif b == "R": r+=a
    else: s+=a
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
pc = c/total*100.00
pr = r/total*100.00
ps = s/total*100.00
print(f"Percentual de coelhos: {pc:.2f} %")
print(f"Percentual de ratos: {pr:.2f} %")
print(f"Percentual de sapos: {ps:.2f} %")
