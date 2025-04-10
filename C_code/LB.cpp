#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;


typedef struct Node 
{
    int data;
    struct Node* next;
}Node;

int main()
{
    int k;
    char pan;
    Node *p, *head, *tail;

    p = (Node*)malloc(sizeof(Node));
    head = p;
    tail = p;
    head->next = NULL;

    printf("输入链表节数:");
    scanf("%d",&k);
    for(int i = 0; i < k; i++)
    {
        p = (Node*)malloc(sizeof(Node));
        printf("输入数据:");
        scanf("%d",&p->data);
        tail->next = p;
        tail = p;
        tail->next = NULL;
    }
    p = head->next;
    while(p != NULL)
    {
        printf("数据为:%d\n",p->data);
        p = p->next;
    }
}