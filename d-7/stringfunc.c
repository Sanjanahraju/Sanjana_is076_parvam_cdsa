#include<stdio.h>
#include<string.h>
void main(){
    char arr[15]={'C','i','t','y',' ','C','o','l','l','e','g','e','\0'};
    // count the number of characters and stores in the count in length
    int length =strlen(arr);  //arr as a parameter //strlen is a bulit function of string               
    printf("total length=%d\n",length);

    char str1[20]="city engineering";
    char str3[20]="college";
    strcat(str1,str2);
    printf("%s",str1); //the concatenated string is stored in str1

}