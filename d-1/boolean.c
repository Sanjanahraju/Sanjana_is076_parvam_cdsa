#include<stdio.h>
#include<stdbool.h>
int main(){
    bool b=true;
    int a=3; //if odd number yes if even number it is no
    for(int i=2;i<a;i++){
        if(a%i==0){
            b=false;
            break;
        }
    }
    if(b==true){
        printf("yes");
    }
    else{
        printf("no");
    }
}