"""
Beecrowd
Problema 2544 Kage Bunshin no Jutsu
Link:https://www.beecrowd.com.br/judge/es/problems/view/2544
Se imprime el valor logarítmico en base 2 de la entrada ya que la cantidad de clones de sombra existentes usada X veces la técnica es 2^X
"""
import sys
import math
for line in sys.stdin:
    print(int(math.log2(int(line))))
