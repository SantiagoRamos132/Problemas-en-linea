"""
CodeChef
Problema HIT 
Link: https://www.codechef.com/problems/HIT
La idea es guardar las notas en una lista y ordenarlas, en 4 listas (A,B,C,D) poner en grupos de N/4 las notas de los estudiantes, donde A tiene
las mayores notas y D las menores. A partir de aquí, se busca si la mayor nota de uno de estos grupos es igual a la menor nota del grupo siguiente, si esto sucede
una vez, se imprime -1, sino, se imprime las menores ntoas C, B y A.
"""
t = int(input())
for _ in range(t):
	n = int(input())
	notas = list(map(int,input().split()))
	divisor = n//4
	notas.sort()
	A = notas[divisor*3:divisor*4]
	B = notas[divisor*2:divisor*3]
	C = notas[divisor:divisor*2]
	D = notas[:divisor]
	if D[-1] == C[0] or C[-1] == B[0] or B[-1] == A[0]:
		print(-1)
	else:
		print(C[0],B[0],A[0])
