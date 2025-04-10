#include<stdio.h>

struct Date
{
    int m;
    int d;
    int h;
};

struct Student
{
    char Name[20];
    char Sex[10];
    int Age;
    int Num;
    struct Date m;
}stu = {"Mike", "man", 19, 200, {2,3,4}};

int main()
{
    struct Student* pStu;
    pStu = &stu;
    printf("%d\n",pStu -> Age);
    printf("%d",pStu -> m.d);
}