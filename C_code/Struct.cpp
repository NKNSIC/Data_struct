#include<stdio.h>
#include<iostream>

//第一类定义法（主函数内定义）
struct a
{
    char a1[10];
    int a2;
};

//第二类定义法（体处定义）
struct b
{
    char b1[10];
    int b2;
}b_1={"qwer", 20};

//第三类定义法（直接将C作为数据类型定义）
typedef struct c
{
    char c1[10];
    int c2;
}C;

//第四类定义法
struct
{
    char d1[10];
    int d2;
}d_1 = {"qwer", 20};


//第五类定义法
typedef struct
{
    char e1[10];
    int e2;
}E;


int main()
{
    //第一类定义法
    struct a a_1 = {"qwer", 20};

    //第三类定义法
    C c_1 = {"qwer", 20};

    C* pc = &c_1;
    printf("%s",pc->c1);
}