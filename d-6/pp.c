#include<stdio.h>
void main() {
    int t=700;
    int *p=&t; //p and &t hv same address value
    int **pptr=&p;
    printf(" %d\t%d\t%d\n",t,*p,**pptr); //increment values are printed
    (**pptr)++;
    printf(" %d\t%d\t%d\n",t,*p,**pptr);

    printf(" %x\t%x\n",p,&t);

    printf(" %x\t%x\n",&p,*pptr);

     printf(" %x\t%x\n",&p,pptr);

     pptr=NULL; //Null pointer or wild pointer
     //not pointing to anything //Delink p from t
     printf(" -------------------------\n");
     printf(" %d\n",t);
     printf(" *p=%d\n",*p);
     printf(" **pptr=%d\n", **pptr);






}