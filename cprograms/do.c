#include<stdio.h>
void main() {
    int i=5,j=10;
    do
    {
        printf("I=%d\n",i);
    }while(i<j--);

    do{
        printf(" *******\n");    
    }while(0);
}