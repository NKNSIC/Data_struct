#include<stdio.h>
#include<stdlib.h>

typedef struct student
{
    int num;
    struct student* next;
}STU;

void creat_chain(STU*, STU*, int);
void insert_head(STU*, STU*, int);
void insert_tail(STU*, int);
void insert_inside(STU*,int ,int);

int main()
{
    STU *head, *tail, *p;
    creat_chain(head, tail, 23);
}

void creat_chain(STU* head, STU* tail, int data)
{
    STU* k;
    k = (STU*)malloc(sizeof(STU));
    k->num = data;
    k->next = NULL;
    head = k;
    tail = k;
}

void insert_head(STU* head, STU* p, int data)
{
    STU* k;
    k = (STU*)malloc(sizeof(STU));
    k->num = data;
    k->next = head;
    head = k;
    p = head;
}

void insert_tail(STU* tail, int data)
{
    STU* k;
    k = (STU*)malloc(sizeof(STU));
    k->num = data;
    k->next = NULL;
    tail->next = k;
    tail = k;
}

void insert_inside(STU* p,int index,int data)
{
    STU* k;
    k = (STU*)malloc(sizeof(STU))
}