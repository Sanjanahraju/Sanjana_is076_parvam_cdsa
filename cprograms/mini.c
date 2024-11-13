#include<stdio.h>
#include<stdlib.h>
int main(){
    int num1,num2,x;
    printf("enter num1");
    scanf("%d\n", &num1)
    printf("enter num2");
    scanf("%d\n", &num2)
    
    switch(x){
        case 1:
        printf("press 1 to add");
        break;
        case 2:
        printf("press 2 to subtract");
        break;
        case 3:
        printf("press 3 to multiplication");
        break;
        case 4:
        printf("press 4 to division");
        break;
        default:
        printf(" no operation");
        break;
    }

}