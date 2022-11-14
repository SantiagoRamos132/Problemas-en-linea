"""
Beecrowd
Problema 2582 System of a Download
Link:https://www.beecrowd.com.br/judge/es/problems/view/2582
Se crea una lista con el orden dado en el problema, y por cada entrada leída, se imprime la canción en la posición a+b
de la lista.
"""
Lista = ["PROXYCITY","P.Y.N.G.","DNSUEY!","SERVERS","HOST!","CRIPTONIZE","OFFLINE DAY","SALT","ANSWER!","RAR?","WIFI ANTENNAS"]
C = int(input())
for _ in range(C):
    a,b= map(int,input().split())
    print (Lista[a+b])