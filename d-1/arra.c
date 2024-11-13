#include<stdio.h>
void main(){
    int arr[]= { 4,5,6,200,13,7};
    arr[1]=30;

    int *p=&arr[0];
    printf(" %d\n",arr[0]); //first value printed
    printf(" %d\n",*p);     //first value printed   ARR[0] AND *P SAME

    printf(" %d\n",arr[3]); //4th value printed
    printf(" %d\n",*(p+3));
     //*p means first value  arr[0] adding +3 so it will print arr[0,1,2,3] i.e is4th value i.e is 200

    printf("%x\t%x\n",p,arr); // P AND ARR PRINTS ADDRESS OF FIRST ELEMENT
    printf("%x\t%x\t%x\n",p,arr,&arr[0]); // P and ARR and &ARR are same it prints address

    printf("%d\n",arr[5]); // arr[0,1,2,3,4,5] i.e is last value 7

    printf(" %d\n",*(p+5)); 
    //*p meand arr[0] so +5 means arr[0,1,2,3,4,5] last vcalue of arr[5] is printed i.e 7

    printf(" p=%x\n",p); // p still prints the address of first element 
    p++; //p is incremented by 1 so P  prints the value of 2nd element
    printf("%x\t%d\n",p,*p); //*p prints 2nd element value arr[1] value is 30 
    p++;
    printf("%x\t%d\n",p,*p); //p incremented again next address is printed *p prints nxt value
    p=p+3;
    printf("%x\t%d\n",p,*p); 
    p -=2; //here p is decremented
    printf("%x\t%d\n",p,*p);
    //arr ++;
    




}