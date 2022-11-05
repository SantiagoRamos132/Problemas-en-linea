"""
Beecrowd
Problema 1848 Counting Crow
Link:https://www.beecrowd.com.br/judge/es/problems/view/1848
Se hace la traducción de cada parpadeo de la vaca a binario y se suma el resultado a una variable de suma, esto se
repite hasta que la vaca grita, en ese caso, se imprime el resultado de la variable suma y se pasa a 0. El programa acaba
cuando la vaca grita 3 veces.
"""
def darvueltastring(string):
    resp = ""
    for i in string:
        resp = i+resp
    return resp
def traductor(string):
    vuelto = darvueltastring(string)
    resp = 0
    for i in range(3):
        if vuelto[i] == "*":
            resp+= 1<<i
    return resp
suma = 0
caws = 0
while caws!=3:
    x = input()
    if len(x)==3:
        suma+=traductor(x)
    else:
        print(suma)
        suma = 0
        caws+=1