"""
Beecrowd
Problema 2235 Walking in Time
Link:https://www.beecrowd.com.br/judge/es/problems/view/2235
La idea es que dados los tres créditos, ver si se puede hacer un viaje al pasado o al futuro y volver al presente con solo dos
créditos (esto sucede cuando ambos créditos son iguales, es decir, puedo viajar al pasado N años y del pasado viajar al futuro
N años, con lo que se regresa al presente, o viajar primero N años al futuro y de este futuro N años al pasado) o si se puede realizar la misma acción con tres créditos (si la cantidad de años a viajar usando dos créditos es igual a la del otro crédito no usado). En caso de que sea posible, se imprime "S", y si no
"N".
"""
a,b,c = map(int,input().split())
if a == b or b ==c or a==c or a+b == c or b+c == a or a+c == b:
    print("S")
else:
    print("N")
