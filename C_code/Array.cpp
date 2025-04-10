#include<stdio.h>
#include<iostream>
using namespace std;

int main(void)
{
    int a = 1;
    int b = 11;
    do{
        b %= 2;
        a += b;
    }while(b>1);
    printf("%d",a);
}