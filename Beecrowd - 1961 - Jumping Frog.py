"""
Beecrowd
Problema 1961 Jumping Frog
Link:https://www.beecrowd.com.br/judge/es/problems/view/1961
Se calcula la distancia entre cada tubo usando el valor absoluto de la altura del tubo i - la altura del tubo i+1,
y si la diferencia es mayor a la altura de salto de la rana, se imprime que el juego no se puede terminar.
"""
a,b = map(int,input().split())
l = list(map(int,input().split()))
for i in range(len(l)-1):
    if abs(l[i]-l[i+1]) >a:
        print("GAME OVER")
        quit()
print("YOU WIN")
