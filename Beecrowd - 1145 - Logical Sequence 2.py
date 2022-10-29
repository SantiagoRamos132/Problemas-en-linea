"""
Beecrowd
Problema 1145 Logical Sequence 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/1145
Se leen dos números "X" y "Y", y se imprimen los números desde 1 hasta "Y", de manera que por cada línea se impriman los números en grupos de "X".
"""
x,y = map(int,input().split())
for i in range(1,y+1):
    if i%x == 0:
        print (i,end="\n")
    else: 
        print(i,end=" ")
