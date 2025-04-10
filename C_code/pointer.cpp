#include<stdio.h>
/*
*指针运算符：使用订单号取餐
*取地址算符：得到餐的订单号
*/
void swap(int*,int*);

int
main(void)
{
    int x,y;
    int* pa;                 /*定义基类型为int的指针*/
    int a = 2,b = 2,c;
    pa = &a;                 /*将pa指向a*/
    c = *pa + b;             /*使用*运算将所指向的数据取出*/
    printf("%d",c);
    printf("input :");
    scanf("%d,%d",&x,&y);
    swap(&x,&y);
    printf("%d,%d",x,y);
}

/*交换两个数值，因实形参在调取完后便不会有联系
所以我们在地址层面上进行交换操作*/
void
swap( int* px, int* py )
{
    int t;
    t = *px; *px = *py; *py = t;
}