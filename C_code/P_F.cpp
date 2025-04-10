#include<stdio.h>

char* month(int);

int main()
{
    int n;
    printf("sfdgfyhtrgrfedadesfdthyu\n");
    scanf("%d",&n);
    printf("%s",month(n));
}

char* month(int n)
{
    char* month[]=
    {
        "?",
        "qwe",
        "qwert",
        "qwt",
    };
    return (n>0 && n<5)?month[n]:month[0];
}