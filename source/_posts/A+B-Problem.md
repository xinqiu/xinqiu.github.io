---
title: HDOJ - 1000  A + B Problem
date: 2015-1-4
tags: [ACM,HDOJ,code]
---

# A + B Problem

Calculate a + b

## Input

The input will consist of a series of pairs of integers a and b,separated by a space, one pair of integers per line.

## Output

For each pair of input integers a and b you should output the sum of a and b in one line,and with one line of output for each line in input.

<!-- more -->

## Sample Input

1 1

## Sample Output

2


```c
#include <stdio.h>
int main()
{
	int a,b;
	while(scanf("%d %d",&a,&b)!=EOF)
		printf("%d\n",a+b);
	return 0;
}
```
