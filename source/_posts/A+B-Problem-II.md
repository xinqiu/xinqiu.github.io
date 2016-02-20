---
layout: post
title: HDOJ - 1002  A + B Problem II
date: 2015-2-3
description: "HDOJ ACM"
tags: [ACM,HDOJ,code]
---
# A + B Problem II

AC了半天，老是一些细节没注意。

## Problem Description
I have a very simple problem for you. Given two integers A and B, your job is to calculate the Sum of A + B.
 

## Input
The first line of the input contains an integer T(1<=T<=20) which means the number of test cases. Then T lines follow, each line consists of two positive integers, A and B. Notice that the integers are very large, that means you should not process them by using 32-bit integer. You may assume the length of each integer will not exceed 1000.
 

## Output
For each test case, you should output two lines. The first line is "Case #:", # means the number of the test case. The second line is the an equation "A + B = Sum", Sum means the result of A + B. Note there are some spaces int the equation. Output a blank line between two test cases.
 
<!-- more -->

## Sample Input
2

1 2

112233445566778899 998877665544332211
 

## Sample Output
Case 1:

1 + 2 = 3

Case 2:

112233445566778899 + 998877665544332211 = 1111111111111111110


```c
#include <stdio.h>
#include <string.h>
int main()
{
    char s1[1000],s2[1000];
    int a[1001]={0};
    int i,j = 1,n,n1,n2;
    int len;
    scanf("%d",&n);
    while (n--) {
        scanf("%s %s",s1,s2);
        printf("Case %d:\n",j++);
        printf("%s + %s = ",s1,s2);
        n1 =(int) strlen(s1)-1;
        n2 = (int) strlen(s2)-1;
        len = (n1>n2?n1:n2)+1;
        for (i = 0; n1 >= 0 || n2 >= 0; i++,n1--,n2--) {
            if(n1>=0&&n2>=0){a[i]=s1[n1]+s2[n2]-48-48;}
            if(n1>=0&&n2<0){a[i]=s1[n1]-48;}
            if(n1<0&&n2>=0){a[i]=s2[n2]-48;}
        }
        for(i=0;i<len;i++)
        {
            if(a[i] >= 10)
            {
                a[i] -= 10;
                a[i+1] += 1;
            }
        }
        if (a[len] ==1 )
            len += 1;
        while (len--)
            printf("%d",a[len]);
        if(n!=0)
            printf("\n\n");
        else
            printf("\n");
    }
    return 0;
}
```