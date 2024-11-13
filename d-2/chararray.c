#include<stdio.h>
int main(){
    int c=0;
    int a[]={10,25,30,40,55};
    int n=sizeof(a)/sizeof(a[0]); //n=5 this line is used to fins the length
    for(int i=n-1;i>0;i--)
    if(a[i]%2==1){ //to print even numbers
        printf("%d\n\n\n",a[i]);
    }

    for(int i=n-1;i>=0;i--){  //printing of elements from last
    printf("%d\n\n\n",a[i]);
    }

    for(int i=0;i<n;i++)
    c=c+a[i];
    printf("%d\n",c);




   
}