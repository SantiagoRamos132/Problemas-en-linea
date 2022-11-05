"""
Beecrowd
Problema 1564 Brazil World Cup
Link:https://www.beecrowd.com.br/judge/es/problems/view/1564
La idea es que por cada entrada que se lea, si el número de entrada es un 0, se imprima "vai ter copa!", y si no, imprimir
"vai ter duas!".
"""
from sys import stdin

for line in stdin:
  x = int(line)
  if x==0:
      print("vai ter copa!")
  else:
      print("vai ter duas!")
