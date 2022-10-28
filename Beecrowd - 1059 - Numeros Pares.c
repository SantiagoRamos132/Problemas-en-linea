/*
Beecrowd
Problema 1059 Números Pares
Link:https://www.beecrowd.com.br/judge/es/problems/view/1059
Se usa un for que recorre los numeros del 1 al 100 y va imprimiendo los números impares. (numeros que al divirlos por 2
den residuo 0)
*/
#include <stdio.h>
 
int main() {
    for(int i=1;i<101;i++){
        if (i%2==0){
            printf("%d\n",i);
        }
    }
    return 0;
}
