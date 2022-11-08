"""
Beecrowd
Problema 2165 Twitting
Link:https://www.beecrowd.com.br/judge/es/problems/view/2165
La idea es guardar la entrada como un string, y si el tamaño de este string es mayor a 140, se imprime "MUTE", si no,
"TWEET"
"""
t = input()
if len(t) >140:
    print("MUTE")
else:print("TWEET")