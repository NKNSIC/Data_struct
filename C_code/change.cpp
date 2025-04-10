
#include<stdio.h>
void change(int a[]);
int t;
int main(void)
{
    int a[5];
    int c;
    printf("Please input the array :");
    for(int i =0; i < 5; i++)
    {
        scanf("%d",&a[i]);
    }
    change(a);
}

void 
change(int a[])
{
    for(int i = 0; i < 4; i++)
    {
        for(int j = i + 1;j < 5; j++)
        {
            if( a[i] > a[j] )
            {
                t = a[i];
                a[i] = a[j];
                a[j] = t;          
            }
        }
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%d ",a[i]);
    }
}

