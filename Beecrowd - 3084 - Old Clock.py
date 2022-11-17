"""
Beecrowd
Problema 3084 Old Clock
Link:https://www.beecrowd.com.br/judge/es/problems/view/3084
Se divide la hora entre 30 ya que es el ángulo que hay entre cada hora, y los minutos entre 6 por la misma razón,
después se imprime la hora en el fórmato de horas:minutos.
"""
import sys
for line in sys.stdin:
    h,m = map(int,line.split())
    h//=30
    m//=6
    if h<10:
        h=f"0{h}"
    if m<10:
        m=f"0{m}"
    print(f"{h}:{m}")
