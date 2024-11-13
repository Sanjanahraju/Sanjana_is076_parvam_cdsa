#include<stdio.h>
#include<stdlib.h>8
int main(){
    int a=5;
    //printf("enter size");
    //scanf("%d",&a);
    arr=(int *)malloc(a *sizeof(int)); //for malloc //output is garbage       //syntax
    arr[2]=20;
    printf("%d\n",arr[2]);
    

    int *arr=(int *)calloc(a ,sizeof(int)); //for calloc //output is  0     //syntax
    arr[2]=20;
    arr[0]=200;
    printf("%d\n",arr[0]);
    free(arr);  //to get output 0
    printf("%d",arr[0]);
}