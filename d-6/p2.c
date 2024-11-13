int x=10,y=20;
int*const ptr=&x;
*ptr=15;
ptr=&y;
printf("%d",ptr);
10
20
15
compliation error