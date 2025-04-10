#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
using namespace std;
int main()
{
	double a,b,c;
	double Dlta;
	double x1,x2;
	printf("Input a,b,c=");
	scanf("%lf,%lf,%lf",&a,&b,&c);
	Dlta =b*b-4*a*c;
	if(a==0)
	{
		if(b==0)
		{
			cout<<"This equation don't have solution";
		}
		else
		{
			cout<<"This equation have only solution x ="<<b/c;
		}
	}
	else
	{
		if(Dlta < 0)
		{
			cout<<"This equation don't have solution";
		}
		else
		{
			x1 = (-b+sqrt(Dlta))/(2*a);
			x2 = (-b-sqrt(Dlta))/(2*a);
			if(x1==x2)
			{
				cout<<"This equation have only solution x ="<<x1;
			}
			else
			{
				cout<<"This equation have two solutions they are:"<<"x1 ="<<x1<<endl;
				cout<<setw(46)<<"x2 ="<<x2;
			}
		}
	}
}