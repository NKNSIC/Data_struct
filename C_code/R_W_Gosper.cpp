#include<stdio.h>
#include<math.h>

const double e = 2.71828;
const double Pi = 3.1415926535;

int
main(void)
{
    int x;
    double y;
    /**输入想要进行阶乘的数字*/
    printf("Please input the Factoral :");
    scanf("%d",&x);
    /*进行近似公式计算*/
    y = pow(x,x) * pow(e,-x) * sqrt( (2.0 * x + 1./3 ) * Pi );
    /*输出计算结果*/
    printf("The anwser is : %lf",y);
}