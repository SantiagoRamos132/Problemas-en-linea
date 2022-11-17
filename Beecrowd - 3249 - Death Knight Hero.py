"""
Beecrowd
Problema 3249 Death Knight Hero
Link:https://www.beecrowd.com.br/judge/es/problems/view/3249
Se recorre los carácteres de una entrada (batalla), si se encuentra una D después de una C, no se aumenta el contador de 
victorias. Si en una batalla nunca sucede que se encuentre una D después de una C, se aumenta el contador de victorias en
1.
"""
batallas = int(input())
resp = 0
for _ in range(batallas):
    c = False
    cuenta = True
    entrada = input()
    for char in entrada:
        if char =="C":c = True
        elif c:
            if char == "D":
                cuenta = False
            else:
                c = False
    resp+=int(int(cuenta))
print(resp)