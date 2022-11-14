/*
Beecrowd
Problema 2747 Output 1
Link:https://www.beecrowd.com.br/judge/es/problems/view/2747
Se imprime el mensaje indicado. Para imprimir varias veces un carácter en una línea se utilizan for's.
*/
#include <stdio.h>
 
int main() {
    for(int i=0;i<39;i++){
        printf("-");
    }
    printf("\n");
    for(int i =0;i<5;i++){
        printf("|"); //Linea 1, quedan 38 dashes restantes
        for (int i=0;i<37;i++){
            printf(" ");
        }
        printf("|\n");
    }
        for(int i=0;i<39;i++){
        printf("-");
    }
    printf("\n");
    return 0;
}
