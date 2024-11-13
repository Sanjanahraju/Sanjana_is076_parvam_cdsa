#include<stdio.h>
void main(){
    int t=700;
    const int*p=&t;
    //(*p)++;
    t++;
    printf(" %d\n",t);
    (*p)++;
    t++;
    printf("%d\n",t);
    }