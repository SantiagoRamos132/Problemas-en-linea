"""
Beecrowd
Problema 3241 Help a PhD Candidate Out!
Link:https://www.beecrowd.com.br/judge/es/problems/view/3241
Si una entrada es "P=NP", se imprime skipped, sino, se separa la entrada a partir del símbolo de suma y imprime
la suma de los dos enteros resultantes de esa separación.
"""
n = int(input())
for _ in range(n):
    entrada = input()
    if entrada == "P=NP":
        print("skipped")
    else:
        a,b = map(int,entrada.split("+"))
        print(a+b)
