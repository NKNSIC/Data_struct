#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main()
{
    char c[5][10];

    //把后面那个复制到前面那个
    strcpy(c[0],"HELLOW");
    strcpy(c[1],"HEL");
    strcpy(c[2],"HELLOW");
    cout<<c[0]<<endl;

    //字符串比较函数，相当于java中的format，等为0不等为1
    cout<<strcmp(c[0],c[1])<<endl; 
    cout<<strcmp(c[0],c[2])<<endl;

    //字符串连接函数，连接并赋值到一个数组中
    strcat(c[0],c[1]);
    cout<<c[0]<<endl;

    //串长度函数，计算字符串的长度
    cout<<strlen(c[0]);

    char ch[20];
    gets(ch);
    puts(ch);
}