"""
Beecrowd
Problema 1047 Tiempo de Juego con Minutos
Link:https://www.beecrowd.com.br/judge/es/problems/view/1047
Se obtiene el tiempo transcurrido en minutos desde el inicio del dia 1 (minuto 0, hora 0) hasta el inicio del juego y se guardan en la variable i
Y el tiempo transcurrido en minutos desde el inicio del dia 1 o 2, hasta el final del juego (debido a que 
si termina en el segundo día, el tiempo transcurrido en horas mayor o igual a 24, pero las horas estan dadas
en base 24, por ende no se puede saber si esta hora final fue del dia 0 o del dia 1 con solo el dato de la hora final)
Si los minutos y se guarda en la variable f.
Si f es mayor a i, significa que el inicio y final fue en el mismo dia, por lo que se restan ambas variables, y se obtienen el tiempo pasado
en formato de horas y minutos pasando el resultado de la resta a horas y minutos.
En caso contrario, se le suma a la hora final 1 dia en minutos (para obtener el tiempo transcurrido desde
el dia 1 hasta el final del juego) y se procede de la misma manera.
"""
a,b,x,y = map(int,input().split())
i = a*60+b
f = x*60+y
if i<f:
    print(f"O JOGO DUROU {(f-i)//60} HORA(S) E {(f-i)%60} MINUTO(S)")
else:
    print(f"O JOGO DUROU {((f+(24*60))-i)//60} HORA(S) E {((f+24*60)-i)%60} MINUTO(S)")
