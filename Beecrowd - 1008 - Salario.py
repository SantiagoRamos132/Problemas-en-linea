"""
Beecrowd
Problema 1008 Salario
Link:https://www.beecrowd.com.br/judge/es/problems/view/1008
El programa lee 2 enteros y un flotante, correspondientes a el número de empleado, las horas que trabajó y el monto recibido por hora, luego imprime el número de empleado y el salario que recibirá a fin de mes, que se obtiene multiplicando las horas trabajadas por el monto por hora 	
"""
NUMBER = int(input())
HOURS = float(input())
MONTO = float(input())
print('NUMBER =',NUMBER)
print('SALARY = U$',format((HOURS*MONTO),'.2f'))
