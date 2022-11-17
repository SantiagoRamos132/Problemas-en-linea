"""
Beecrowd
Problema 3147 The Battle of the Five Armies
Link:https://www.beecrowd.com.br/judge/es/problems/view/3147
Si la suma de soldados del ejército del lado bueno es mayor que la del lado malo, se imprime "Middle-earth is safe", si no, se imprime
"Sauron has returned".
"""
H,E,A,O,W,X = map(int,input().split())
if H+E+A+X > O+W:print("Middle-earth is safe.")
else: print("Sauron has returned.")
