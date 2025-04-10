#include<stdio.h>
#include<iomanip>
#include<iostream>

/*定义遍历的项*/
#define N 5

using namespace std;

void print_A(int a[], int);
void swap(int a[], int);

int
main(void)
{
    int a[5] = {10, 3, 34, 3, 4};
    /*实现数组逆置*/
    print_A(a,N);
}

/*遍历数组的函数（老方法）*/
void
print_A(int a[], int n)
{
    for(int i = 0; i < n; i++)
    {
        cout<<setw(5)<<a[i];
    }
}

/*实现数组逆置的函数*/
void
swap(int a[], int n)
{
    int t;
    int* p1;
    int* p2;
    p1 = &a[0];
    p2 = &a[n-1];
    for (p1 < p2; p1++; p2--)
    {
        t = *p1; *p2 = *p1; *p2 = t;
    }
}
