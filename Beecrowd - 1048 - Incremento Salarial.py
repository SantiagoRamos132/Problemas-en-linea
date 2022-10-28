"""
Beecrowd
Problema 1048 Incremento Salarial
Link:https://www.beecrowd.com.br/judge/es/problems/view/1048
Dado el salario, se guarda en la variable p el porcentaje aumentado, y se imprime cuanto dinero se aumento
(sacar el "p" porciento al salario inicial), el nuevo salario y el porcentaje obtenido.
"""
sal = float(input())
if sal >=0 and sal <= 400.00:
    p = 15
elif sal >= 400.01 and sal <= 800.00:
    p = 12
elif sal >= 800.01 and sal <= 1200.00:
    p = 10
elif sal >= 1200.01 and sal <= 2000.00:
    p = 7
if sal > 2000.00:
    p = 4
print(f"Novo salario: {((sal*(100+p))/100.00):.2f}")
print(f"Reajuste ganho: {(sal*(p/100)):.2f}")
print(f"Em percentual: {p} %")