#include<stdio.h>
#include<string.h>

struct stu 
{
    int age;
    int mon;
};

struct stu st[3];
char L[2][4] = {"1st", "2st", "3st"};

void print(struct stu st[3]);
void scan(struct stu st[3]);

int main(void)
{
    struct stu stu[3];
    scan(stu);
    print(stu);
}

void scan(struct stu st[3])
{
    for (int i = 0; i < 3; i++)
    {
        printf("This is the %d", i);
        scanf("please ip age: ", &st[i].age);
        scanf("please ip mon: ", &st[i].mon);
    }
    
}

void print(struct stu st[3])
{
    for (int i = 0; i < 3; i++)
    {
        printf("age = %d\n", st[i].age);
        printf("mon = %d\n", st[i].mon);
    }
}