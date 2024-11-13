#include<stdio.h>
struct student{
    int rollNO; char name[50];int semesterNumber;
    float fee;char course[50];
};
struct student s; //global //s is the variable student is the data type
void main(){
    printf("%d\t\t",s.rollNO);
    printf("%f",s.fee);
    s.rollNO=100; s.fee=52000.00f;
    printf("\n%d\t\t",s.rollNO);
    printf("%f",s.fee);

     
}