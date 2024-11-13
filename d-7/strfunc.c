#include<stdio.h>
void main(){
    int i,count=0;
    char arr[15]={'c','i','t','y','c','o','l','l','g','e','\0'};
    for (int i=0;arr[i]!='\0';i++){
        {printf("%s\t\t",i);
        count++;
        }

    }printf("total length:%d",count);
}
