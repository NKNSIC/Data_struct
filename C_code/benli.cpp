#include<iostream>
using namespace std;
int main(void)
{
    double year = 5;
    double money = 1200;
    double r = 0.03;
    double P;        //本利和
    double p;        //利息
    p = money * year * r;
    P = money + p;
    cout<<P<<endl;
}