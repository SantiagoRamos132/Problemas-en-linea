"""
Beecrowd
Problema 2483 Merry Christmaaas!
Link:https://www.beecrowd.com.br/judge/es/problems/view/2483
Se le agrega "i" veces una a al string de "Feliz nat", y luego de agregar las a's necesarias, se concatena
este string con el string "l!" y se imprime. 
"""
i = int(input())
texto ="Feliz nat"
for i in range(i):
    texto+= "a"
texto+="l!"
print(texto)