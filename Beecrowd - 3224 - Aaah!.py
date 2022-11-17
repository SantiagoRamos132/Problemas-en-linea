"""
Beecrowd
Problema 3224 Aaah!
Link:https://www.beecrowd.com.br/judge/es/problems/view/3224
Si la duración del Ah de Jon es mayor o igual al tiempo mínimo (Tiene una cantidad mayor o igual
de carácteres), se imprime que puede ir al show, sino, se imprime que no puede ir.
"""
x1 = input()
x2 = input()
if len(x1)>=len(x2):
    print("go")
else:print("no")
