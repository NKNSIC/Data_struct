#include<iostream>
#include<stdlib.h>

using namespace std;

int main(void)
{
    
    //定义一个空指针
    int* p = NULL;
    int* d = NULL;

    //malloc函数可以申请适合的内存空间，节省了程序运行空间，从而提高程序的可移植性
    //申请一个四个字节的内存空间，并强制将void指向改为int
    p = (int*)malloc(4);
    //如果我们不知道它占多少字节，我们可以使用sizeof()
    d = (int*)malloc(sizeof(int));

    int n = 10;
    float* pf = NULL;

    //向系统申请了n个连续的float型存储单元，并使pf指向该存储单元的首地址
    pf = (float*)calloc(n,sizeof(float));
    //我们可以使用这种方式去定义数组，可大大减少内存空间
    pf[0] = 3.323;
    printf("%f",pf[0]);

    //free可以释放内存空间
    free(p);
}