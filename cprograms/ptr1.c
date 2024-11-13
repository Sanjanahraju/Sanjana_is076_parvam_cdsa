#include<stdio.h>
void main() {
    int t=1000;
    const int * const p= &t;  //*p and b is constant and cannot be modified
    //(*p)++;
    int d=200;
    //p=&d;
    t++;
    printf("%d\n",t);

