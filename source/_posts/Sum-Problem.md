---
title: HDOJ - 1001  Sum Problem
date: 2015-1-5
tags: [ACM,HDOJ,code]
---

# Sum Problem


## Problem Description

Hey, welcome to HDOJ(Hangzhou Dianzi University Online Judge).

In this problem, your task is to calculate SUM(n) = 1 + 2 + 3 + ... + n.
 

## Input

The input will consist of a series of integers n, one integer per line.
 

## Output
For each case, output SUM(n) in one line, followed by a blank line. You may assume the result will be in the range of 32-bit signed integer.
 
 <!-- more -->

## Sample Input
1
100
 

## Sample Output
1

5050

```c
//递归
#include <stdio.h>
int sum(int n)
{
	if (n==1)
		return 1;
	else
		return n+sum(n-1);
}
int main()
{
	int n;
	while(scanf("%d",&n)!=EOF)
		printf("%d\n\n",sum(n));
	return 0;
}

//公式
#include <stdio.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
        printf("%f\n\n",((1+n)/2.0*n));
    return 0;
}

```

公式的方法要判断n的奇偶性，因为n*(n+1)可能数字太大。