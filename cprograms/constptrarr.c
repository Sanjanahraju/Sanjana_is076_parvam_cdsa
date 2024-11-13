#include<stdio.h>
void main() {
    //compiler converts this statement into
    //int*const arr={100,290,112,56,289,11}
    int arr[6]={100,290,112,56,289,11};
    int * const ptr=&arr[0]; //const pointer to a constant array
    arr++;
    ptr++;
    arr[2]=25;
    *(ptr+2)=119;
}