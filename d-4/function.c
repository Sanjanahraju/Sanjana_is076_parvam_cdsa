#include<stdio.h>
void sum(int n1, int n2)   //takes 2 paramters
{
   
   int c=n1+n2;   //function definition
   printf("%d\n",c);  //function definition
   n1++;n2++;
   sum(n1,n2);  //function calling itself
}
void main() {
    int a=100,b=200;
    sum(a,b); //function call for 1st time
    printf(" 2 number added...");
}   
