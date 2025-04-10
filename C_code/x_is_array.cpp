#include<iostream>
#include<stdio.h>
#define N 10
using namespace std;
double average(int score[],int);
int main(void)
{
    int score[10];
    cout<<"Please input scores :";
    for( int j = 0; j < N; j++ )
    {
        cin>>score[j];
    }
    double aver = average(score,N);
    cout<<"Average score is "<<aver;
}

double
average( int score[], int n )                      //计算成绩平均值
{
    int sum = 0;
    for( int i =0; i < n; i++ )
    {
        sum += score[i];
    }
    return 1.0 * sum / n;
}