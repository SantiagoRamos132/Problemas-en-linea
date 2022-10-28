"""
Beecrowd
Problema 1061 Tiempo Del Evento
Link:https://www.beecrowd.com.br/judge/es/problems/view/1061
Se obtiene el tiempo transcurrido en segundos desde el inicio del dia 0, hasta tanto el inicio como el final del evento.
Luego restando ambos tiempos se obtiene la duración del evento en formato de días, horas, minutos y segundos.
"""
D1 = int((input().split())[1])
H1,M1,S1 = map(int,(input().split(" : ")))
D2 = int((input().split())[1])
H2,M2,S2 = map(int,(input().split(" : ")))

T1 = S1+M1*60+H1*60*60+D1*24*60*60
T2 = S2+M2*60+H2*60*60+D2*24*60*60

Dia = (T2-T1)//(24*60*60)
Resto = (T2-T1)%(24*60*60)
Horas = (Resto)//(60*60)
Resto = (Resto)%(60*60)
Minutos = Resto//(60)
Segundos = Resto%60
print(Dia,"dia(s)")
print(Horas,"hora(s)")
print(Minutos,"minuto(s)")
print(Segundos,"segundo(s)")