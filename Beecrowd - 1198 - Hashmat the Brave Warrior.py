"""
Beecrowd
Problema 1198 Hashmat the Brave Warrior
Link:https://www.beecrowd.com.br/judge/es/problems/view/1198
Se imprime la diferencia entre sus soldados y los soldados enemigos.
"""
import sys
for line in sys.stdin:
    a,b = map(int,line.split())
    print(abs(a-b))