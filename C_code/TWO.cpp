#include<iostream>
#include<stdio.h>
#include<iomanip>
#include<math.h>

double Do_x0(double x,double y);

using namespace std;

int
main()
{
	double d, a, b, c, i, j, k;
	double x0, x1, x2, f0, f1, f2;
	double Dlta;
	printf("Please input d,a,b,c =");
	scanf("%lf,%lf,%lf,%lf",&d,&a,&b,&c);
	if(d==0)
	{
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
	else
	{
		do 
		{
			printf("Input two points:");
			scanf("%lf,%lf", &x1, &x2);
			f1 = d * pow(x1,3) + a * pow(x1,2) + b * x1 + c;
			f2 = d * pow(x2,3) + a * pow(x2,2) + b * x2 + c;
			printf("f1 = %f, f2 = %f\n", f1, f2);
		} while (f1 * f2 > 0);

		do 
		{
			x0 = Do_x0(x1,x2);
			f0 = d * pow(x0,3) + a * pow(x0,2) + b * x0 + c;
			if (f0 * f1 < 0) 
			{
				x2 = x0;
				f2 = f0;
			}
			else 
			{
				x1 = x0;
				f1 = f0;
			}
		} while (fabs(f0) >= 1e-20);
		printf("solution is x =%lf\n", x0);
	}
}

double
Do_x0(double x,double y)
{
	return (x+y)/2.;
}