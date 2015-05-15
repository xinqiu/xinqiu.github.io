---
layout: post
title: 几种常见排序算法的学习
description: "sort algorithm"
tags: [algorithm]
image:
  background: ps_neutral.png
---
#几种常见排序算法的学习

> 排序算法是面试中常被提及的算法种类之一，以下记录了我学排序的一些想法。

###插入排序

#####介绍

插入排序(insertion sort)是最简单的排序算法之一。插入排序由 `N - 1` 趟(pass)排序组成。对于`P = 1` 趟到 `P = N - 1` 趟，插入算法保证从位置 0 到位置 P 上的元素为已排序状态。

```
void InsertionSort(ElementType A[],int N)
{
    int j, P;
    
    ElementType Tmp;
    for(P = 1; P < N; P++)
    {
        Tmp = A[P];
        for(j = P; j > 0 && A[j-1] > Tmp; j--)
            A[j] = A[j-1];
        A[j] = Tmp;
    }
}

```

####插入排序的分析

嵌套循环的每一个都花费 `N` 次迭代,因此插入排序为O(N^2)。



(To be continued)