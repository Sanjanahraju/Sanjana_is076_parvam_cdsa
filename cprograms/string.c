//using array to store the strings

#include<stdio.h>
void main(){
    int j,count = 0;
    char name [12]={'c','i','t','y','c','o','l','l','e','g','e', '\0'}; //each character defined separately
    //printf("%c\n",name[1]); // prints second character in the string
    //printf("%c\n",name[3]);
    //for (int i=4; i>=0;i--){
      //  printf("%c\t",name[i]);
        //puts("\n\n");
        // run the loop till it is null(\0)
    for(int j=0;name[j]!='\0';j++) {
        if(name[j]=='a'||name[j]=='e'||name[j]=='i'||name[j]=='o'||name[j]=='u'||name[j]=='A'||name[j]=='E'||name[j]=='I'||name[j]=='O'||name[j]=='U')
        {printf("%c\t\t",name[j]);
        count++;
        }
    }
    printf("no of vowels:%d",count);
        
}

