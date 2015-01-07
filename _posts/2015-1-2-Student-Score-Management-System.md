---
layout: post
title: C Project-Student Score Management System 
description: "C Project"
tags: [C,code]
image:
  background: geometry.png
---

##	简介

这算是我第一次写这么多代码，还需要润色。这两天写完这么多，感觉对C又有了新的感悟。

实话说，自己也没想到第一次能写这么多代码。大一上学期快结束了，不喜欢学院派的这种应付式的学C，真心想把C学好，这样才能为之后的C++自学之路打下基础。作为新年里第一个计划的完成，元旦终于可以休息一下了。

说起来，寒假得与C做个总结了。下学期开Java课，还必须预习。C++/Python的自学，不知又会怎样。恐怕，会是一段艰苦的时光。

有人说我的梦想像白日梦，我喜欢那句

> 我们的梦想，是星辰大海

但我坚信，只有说出来会被嘲笑的梦想，才值得奋不顾身的去实现。

* * *

### Student Score Management System

{% highlight C %}

//
//  main.c
//  C
//
//  Created by 仇鑫 on 14-12-31.
//  Copyright (c) 2014年 仇鑫. All rights reserved.
//


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LEN sizeof(struct student)
#define NULL 0

typedef struct student      //结构体
{
    int No;
    char Name[20];
    int Chinese;
    int Math;
    int English;
    int Score;
    struct student *next;
}linklist;
linklist *head=NULL,*end;

//初始化
void InitInf()
{
    FILE *fp;
    printf("*************************初始化*************************\n");
    //fp=fopen("data.dat","w+b");//打开二进制文件
    fp=fopen("/Users/qiuxin/Desktop/C/C/data.txt", "wt");//打开文本文件
    fclose(fp);
}

//读取数据
linklist *LoadData()
{
    FILE *fp;
    int i;
    linklist *p1,*p2;
    printf("*************************读取信息*************************\n");
    //fp=fopen("data.dat","r+b");//读取二进制文件
    p1=p2=(linklist *)malloc(LEN);
    if (p1==NULL||p2==NULL) {
        printf("空间不足!\n");
        exit(0);
    }
    //head=NULL;
    fp=fopen("/Users/qiuxin/Desktop/C/C/data.txt","rt");//读取文本文件
    if (fp==NULL) {
        printf("Open File Error!\n");
        exit(0);
    }
    // 读取链表
    else
    {
        while (!feof(fp)) {
            i++;
            fscanf(fp,"%d %s %d %d %d %d",&p1->No,p1->Name,&p1->Chinese,&p1->Math,&p1->English,&p1->Score);
            if (i==1)
                head=p1;
            else
                p2->next=p1;
            p2=p1;
            p1=(linklist *)malloc(LEN);
            if (p1==NULL) {
                printf("空间不足!\n");
                exit(0);
            }

        }
        p2->next=NULL;
        end=p2;
        return head;
    }
}

//检查学号重复的项
//void checkno()

//cheak
void cheak(int p)
{
    while (p<0||p>100) {
        printf("Input score wrong!\n");
        scanf("%d",&p);
    }
}
//从键盘输入学生信息
linklist *InputData()
{
    linklist *p1,*p2;
    int n=0;
    printf("*********************************************************\n");
    printf("                如果没初始化,请输入0返回，先初始化             \n");
    printf("*****************请输入学生信息，输入0结束输入****************\n");
    p1=p2=(struct student *)malloc(LEN);
    if (p1==NULL||p2==NULL) {
        printf("空间不足!\n");
        exit(0);
    }
    /*printf("*********Input No Name Chinese Math and English**********\n********************Input No=0 to End********************\n");
    scanf("%d%s%d%d%d",&p1->No,p1->Name,&p1->Chinese,&p1->Math,&p1->English);
    p1->Score=p1->Chinese+p1->Math+p1->English;
    head=NULL;
    
    while (p1->No!=0) {
        n++;
        if (n==1)
            head=p1;
        else
            p2->next=p1;
        p2=p1;
        p1=(linklist *)malloc(LEN);
        printf("Input No Name Chinese Math and English\nInput No=0 to End\n");
        scanf("%d%s%d%d%d",&p1->No,p1->Name,&p1->Chinese,&p1->Math,&p1->English);
        p1->Score=p1->Chinese+p1->Math+p1->English;
    }
    p2->next=NULL;*/
    printf("Please Input No:\nInput No=0 to End\n");
    scanf("%d",&p1->No);
    while (p1->No!=0) {
        if (p1->No<0) {
            printf("Sthudent N0 wrong\nPlease input again\n");
            scanf("%d",&p1->No);
            continue;
        }
        n++;
        printf("Please Input Name Chinese Math English:\n");
        scanf("%s%d%d%d",p1->Name,&p1->Chinese,&p1->Math,&p1->English);
        /*while (p1->English<0||p1->English>100) {
         printf("Input score wrong!\n");
         scanf("%d",&p1->English);
         }*/
        cheak(p1->Chinese);
        cheak(p1->Math);
        cheak(p1->English);
        p1->Score=p1->Chinese+p1->Math+p1->English;
        if (n==1)
            head=p1;
        else
            p2->next=p1;
        p2=p1;
        p1=(struct student *)malloc(LEN);
        if (p1==NULL) {
            printf("空间不足!\n");
            exit(0);
        }
        printf("Please Input No:\nInput No=0 to End\n");
        scanf("%d",&p1->No);
    }
    p2->next=NULL;
    end=p2;
    return (head);
}

//添加
linklist *AddStuInf(linklist *end)
{
    linklist *p;//*p1;
//    p1=head;
//    while(p1->next!=NULL)
//    {
//        p1=p1->next;
//    }
    printf("*************************请输入学生信息************************\n");
    p=(struct student *)malloc(LEN);
    if (p==NULL) {
        printf("空间不足!\n");
        exit(0);
    }
//    p1->next=p;
    p=end;
    printf("Please Input No:\n");
    scanf("%d",&p->No);
    while(p->No<0) {
        printf("Sthudent N0 wrong\nPlease input again\n");
        scanf("%d",&p->No);
    }
    printf("Please Input Name Chinese Math English:\n");
    scanf("%s%d%d%d",p->Name,&p->Chinese,&p->Math,&p->English);
    cheak(p->Chinese);
    cheak(p->Math);
    cheak(p->English);
    p->Score=p->Chinese+p->Math+p->English;
    p->next=NULL;
    end=p;
    return head;
}

//删除
linklist *DeletStuInf(linklist *head)
{
    linklist *p1,*p2 = NULL;
    int n;
    printf("*********************************************************\n");
    printf("                   请输入需要删除的学生学号                  \n");
    printf("No:");
    scanf("%d",&n);
    if (head == NULL)
    {
        printf ("\nlinklist null !\n");
    }
    p1 = head;
    while (p1->No != n && p1->next != NULL)
    {
        p2 = p1;
        p1 = p1->next;
    }
    if (n == p1->No)
    {
        if (p1 == head)
        {
            head = p1->next;
            free(p1);
        }
        else
        {
            p2->next = p1->next;
            free(p1);
        }
     }
    else
    {
        printf ("No found! \n");
    }
    return head;
}

    /*
    while(p->No!=n)
    {
        p=p->next;
    }
    if (p==head) {
        head=p->next;
        free(p);
    }
    else if (p==end)
    {
        p1=head;
        while (p1->next!=end) {
            p1=p1->next;
        }
        p1=end;
        p1->next=NULL;
        free(p);
    }
    else
    {
        p1=head;
        while (p1->next!=p) {
            p1=p1->next;
        }
        p1->next=p->next;
        free(p);
    }
     */

//修改
void ModifyStuInf()
{
    int n;
    linklist *p=head;
    printf("*********************************************************\n");
    printf("                请输入需要修改的学生的学号                   \n");
    scanf("%d",&n);
    while (p!=NULL) {
        if (p->No==n) {
            printf("请输入修改后的学生全部信息\n");
            scanf("%s%d%d%d",p->Name,&p->Chinese,&p->Math,&p->English);
            cheak(p->Chinese);
            cheak(p->Math);
            cheak(p->English);
            p->Score=p->Chinese+p->Math+p->English;
            break;
        }
        p=p->next;
    }
    if(p==NULL)
    {
        printf("*********************************************************\n");
        printf("No Found!\n");
        printf("*********************************************************\n");
    }
    getchar();
    return ;
}

//功能菜单
void DataEditMenu()
{
    char MenuItem;
    while (1) {
        printf("*********************************************************\n");
        printf("              Edit Students Information Menu             \n");
        printf("*********************************************************\n");
        printf("*              1-------Add Record                       *\n");
        printf("*              2-------Delete Record                    *\n");
        printf("*              3-------Modify Record                    *\n");
        printf("*              4-------Retrun                           *\n");
        printf("*********************************************************\n");
        do {
            printf("               Please Select an Option(1-4):\n");
            fflush(stdin);    //Clear Buffer
            scanf("%c",&MenuItem);
            getchar();
        }while (MenuItem<'1'||MenuItem>'4');
        switch (MenuItem)
        {
            case '1':
                head=AddStuInf(end);
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '2':
                head=DeletStuInf(head);
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '3':
                ModifyStuInf();
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '4':
                return;
        }
    }
}

//学号查询
void QueryInfByNo(linklist *head)
{
    linklist *p=head;
    int n;
    printf("Input No:\n");
    scanf("%d",&n);
    while (p!=NULL) {
        if (p->No==n) {
            printf("*********************************************************\n");
            printf("No:%d\nName:%s\nChinese:%d\nMath:%d\nEnglish:%d\nScore:%d\n",p->No,p->Name,p->Chinese,p->Math,p->English,p->Score);
            printf("*********************************************************\n");
            break;
        }
        p=p->next;
    }
    if(p==NULL)
    {
        printf("*********************************************************\n");
        printf("No Found!\n");
        printf("*********************************************************\n");
    }
    printf("Press Any Key to Continue.\n");
    getchar();
    return ;
}

//名字查询
void QueryInfByName(linklist *head)
{
    linklist *p=head;
    char name[20];
    printf("Input Name:\n");
    scanf("%s",name);
    while (p!=NULL) {
        if (strcmp(p->Name,name)==0) {
            printf("*********************************************************\n");
            printf("No:%d\nName:%s\nChinese:%d\nMath:%d\nEnglish:%d\nScore:%d\n",p->No,p->Name,p->Chinese,p->Math,p->English,p->Score);
            printf("*********************************************************\n");
            break;
        }
        p=p->next;
    }
    if(p==NULL)
    {
        printf("*********************************************************\n");
        printf("No Found!\n");
        printf("*********************************************************\n");
    }
    printf("Press Any Key to Continue.\n");
    getchar();
    return ;
}

//查询菜单
void DataQueryMenu()
{
    char MenuItem;
    while (1) {
        printf("*********************************************************\n");
        printf("              Edit Students Information Menu             \n");
        printf("*********************************************************\n");
        printf("*              1-------Query by No                      *\n");
        printf("*              2-------Query by Name                    *\n");
        printf("*              3-------Retrun                           *\n");
        printf("*********************************************************\n");
        do {
            printf("               Please Select an Option(1-3):\n");
            fflush(stdin);    //Clear Buffer
            scanf("%c",&MenuItem);
//            getchar();
        }while (MenuItem<'1'||MenuItem>'3');
        switch (MenuItem)
        {
            case '1':
                QueryInfByNo(head);
//                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '2':
                QueryInfByName(head);
//                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '3':
                return;
        }
    }

}


//统计信息
void StatisticStuData(linklist *head)
{
    int n=0;
    long int sum=0;
    double average=0;
    linklist *p=head;
    printf("*********************************************************\n");
    printf("*************************信息统计*************************\n");
    while(p!=NULL){
        n++;
        sum+=p->Score;
        p=p->next;
    }
    average=(double)sum*1.0/n;
    printf("人数:%d\n总分:%ld\n平均分:%f\n",n,sum,average);
}

//写入文件
void SavaDataToFile(linklist *head)
{
    FILE *fp;
    linklist *p;
    fp=fopen("/Users/qiuxin/Desktop/C/C/data.txt", "wt+");
    p=head;
    while (p!=NULL) {
        fprintf(fp,"%d  %s  %d  %d  %d  %d\n",p->No,p->Name,p->Chinese,p->Math,p->English,p->Score);
        p=p->next;
    }
    printf("**************************保存信息*************************\n");
    fclose(fp);
}

//显示学生信息
void DisplayStuInf(linklist *head)
{
    linklist *p;
    p=head;
    printf("*********************************************************\n");
    printf("    学号    姓名       语文      数学       英语      总分\n");
    do {
        printf("%5d%10s      %3d       %3d       %3d       %3d\n",p->No,p->Name,p->Chinese,p->Math,p->English,p->Score);
        p=p->next;
    } while (p!=NULL);
    printf("*********************************************************\n");
}

void DisplayMenu()
{
    char MenuItem;
    while (1) {
        printf("\n");
        printf("*************Students Score Management System************\n");
        printf("*********************************************************\n");
        printf("                        Menu Items                       \n");
        printf("*********************************************************\n");
        printf("*         1-------System Initialize                     *\n");
        printf("*         2-------Data Loading                          *\n");
        printf("*         3-------Input Students Information            *\n");
        printf("*         4-------Edit Students Information             *\n");
        printf("*         5-------Query Students Information            *\n");
        printf("*         6-------Statistic Students Information        *\n");
        printf("*         7-------Output Students Information           *\n");
        printf("*         8-------Display Students Information          *\n");
        printf("*         0-------Exit System                           *\n");
        printf("*********************************************************\n");
        do{
            printf("               Please Select an Option(0-8):\n");
            fflush(stdin);    //Clear Buffer
            scanf("%c",&MenuItem);
            getchar();
        }while (MenuItem<'0'||MenuItem>'8');
        switch (MenuItem) {
            case '1':
                InitInf();
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '2':
                head=LoadData();
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '3':
                head=InputData();
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '4':
                DataEditMenu();
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '5':
                DataQueryMenu();
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '6':
                StatisticStuData(head);
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '7':
                SavaDataToFile(head);
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '8':
                DisplayStuInf(head);
                printf("Press Any Key to Continue.\n");
                getchar();
                break;
            case '0':
                printf("*************Thank you for using this System*************\n");
                exit(0);
             }
    }
    
}

int main(int argc, char const *argv[])
{
    DisplayMenu();
    return 0;
}
{% endhighlight %}
