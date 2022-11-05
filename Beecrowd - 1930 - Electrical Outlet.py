"""
Beecrowd
Problema 1930 Electrical Outlet
Link:https://www.beecrowd.com.br/judge/es/problems/view/1930
Tomando en cuenta que cada dispositivo se conecta a un solo enchufe de un solo tomacorriente, se imprime la suma de todos
los enchufes disponibles - 3, ya que 3 tomacorrientes deben ser enchufados en 3 enchufes para que sirvan.
"""
a,b,c,d = map(int,input().split())
print (a+b+c+d-3) #-3 porque se como son 4 regletas, 3 espacios deben ser usados para contectar 3