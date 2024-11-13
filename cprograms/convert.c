#include<stdio.h>
void main() {
    char ch='b';
    printf("%c\n",ch);
    printf("%d\n",ch);
    int i=ch;
    i-=32;
    printf("%c\n",i);
}