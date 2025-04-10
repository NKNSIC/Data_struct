#include<stdio.h>
#include <stdlib.h>

int main()
{
    FILE* fp;
    char ch[2] = {'A', 'B'};
    char name[2][5] = {"A","B"};
    if ((fp = fopen("T.txt","wb"))==NULL)
    {
        printf("ERROW!!!");
        exit(0);
    }
    fwrite(name[0], 1, 10, fp);
    fclose(fp);
}