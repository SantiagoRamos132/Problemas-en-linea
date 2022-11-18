/*
Beecrowd
Problema 2748 Salida 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/2748
La idea es crear funciones que impriman espacios, las líneas horizontales, las lineas intermedias y un string adentro de las lineas intermedias,
respetando que la cantidad de caracteres en las lineas intermedias es de 37, y usando estas funciones imprimir
la salida dada.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void imprimir_cant_espacios(int n){
    for (int i=0;i<n;i++){
        printf(" ");
    }
}
void imprimir_string(char * string){
    printf("|"); //trazo 1, quedan 38
    imprimir_cant_espacios(8);//ultimo espacio en trazo 9
    printf("%s",string);
    imprimir_cant_espacios(38-(strlen(string)+9));
    printf("|\n");
}
void imprimirLineasintermedias(){
    printf("|");
    imprimir_cant_espacios(37);
    printf("|\n");
}
int main(){
    for (int i=0;i<39;i++){
        printf("-");
    }
    printf("\n");
    imprimir_string("Roberto");
    imprimirLineasintermedias();
    imprimir_string("5786");
    imprimirLineasintermedias();
    imprimir_string("UNIFEI");
    for (int i=0;i<39;i++){
        printf("-");
    }
    printf("\n");

    return 0;
}