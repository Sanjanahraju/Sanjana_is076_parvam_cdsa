#include<stdio.h>
void main(){
    int numbers[5]={100,23,56,278,10}; //array size is 5 and 5 values are given
    printf("%d\n",numbers[0]); //here first value of the array is printed
    printf("%d\n",numbers[1]); //next value is printed
    printf("%d\n", *(numbers+2)); 
       // * is used for incrementation. here numbers incremented by 2 times so third value i.e 56 is printed
      //(numbers+2*2)
      //*(numbers+2*2)
    numbers[2]=800; //here  we declared number2 is 800
    *(numbers+2)=1000; //incremented by 2 so we get the value 800+200=1000
    printf("%d\n",numbers[2]);   
}   