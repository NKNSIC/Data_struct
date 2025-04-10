#include<stdio.h>
#include<math.h>

int
main(void)
{
    float wt_kg, wt_lb, ht_cm, ht_in, BMI;
    printf("Please input the weight(kg) :");
    scanf("%f",&wt_kg);
    printf("Please input the height(cm) :");
    scanf("%f",&ht_cm);
    
    /*进行单位换算*/
    wt_lb = wt_kg * 0.4536;
    ht_in = ht_cm * 2.54;

    /*计算BMI*/
    BMI = 1.0 * wt_lb / ( ht_in * ht_in );

    /*判断身体体质所处于的类型*/
    if( BMI < 18.5 )
        printf("偏轻");
    else if( (BMI >= 18.5)&&(BMI < 24.9) )
        printf("正常");
    else if( (BMI >= 24.9)&&(BMI < 29.9) )
        printf("超重");
    else
        printf("肥胖");
}