#include<stdio.h>
void main() {
    int i=100, j=2, c=i / 2;
    float f=3.4f; //to specify it should be in float
    float t=5.4; //even without f it automatically takes here float
    float o=100.00F;
    printf("%2f\n",(o/j)); // only f means 6 zeros comes , if 2f given after point only 2 zeros print

    //casting (data_type). in c language casting is optional

    int n=f; //here f value 3.4 is assigned to n where n is integer so n takes only 3 doesnot take .4
    printf("%d\n",n); //narrowing conversion

    int n1=100; float f1=n1; //n1 is of int type f1 is float when n1=f1 then f1 becomes 100.0000 
    printf("%f\n",f1); // widening conversion no loss of data
    }