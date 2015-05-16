---
layout: post
title: 几种常见排序算法的学习
description: "sort algorithm"
tags: [algorithm]
image:
  background: ps_neutral.png
---


> 排序算法是面试中常被提及的算法种类之一，以下记录了我学排序的一些想法。

###插入排序

####介绍

插入排序(insertion sort)是最简单的排序算法之一。插入排序由 `N - 1` 趟(pass)排序组成。对于`P = 1` 趟到 `P = N - 1` 趟，插入算法保证从位置 0 到位置 P 上的元素为已排序状态。

{% highlight c %}
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

{% endhighlight %}

####插入排序的分析

嵌套循环的每一个都花费 `N` 次迭代,
对所有的P进行求和，得到总数为
![](http://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D2%7D%5E%7BN%7Di%3D2&plus;3&plus;4&plus;...&plus;N)

因此插入排序为![](http://chart.googleapis.com/chart?cht=tx&chl=O(N^{2}\))。

####总结

其实就是从左到右，取每个元素，通过比较让其放在正确的位置。相比同样是![](http://www.forkosh.com/mathtex.cgi?%20O(N^{2}\))的冒泡排序，插入排序减少了交换元素的次数。

###希尔排序

####介绍

希尔排序(Shellsort)，有时也叫缩小增量排序(deminishing increment sort)，通过比较相距一定间隔的元素来工作；各趟比较所用的距离随着算法的进行而减小，直到只比较相距相邻元素的最后一趟排序为止。

增量的选择有多种，不同的增量，性能也不同。较为常见的是使用希尔增量。以下是以增量为`N / 2`的算法。

{% highlight c %}
void ShellSort(ElementType A[], int N)
{
    int i,j,Increment;
    ElementType Tmp;
    
    for (Increment = N / 2; Increment > 0; Increment /= 2) 
    {
        for (i = Increment; i < N; i++) 
        {
            Tmp = A[i];
            for(j = i; j >= Increment; j-= Increment)
                if (Tmp < A[j - Increment])
                    A[j] = A[j - Increment];
                else
                    break;
            A[j] = Tmp;
        }
    }
}

{% endhighlight %}


(To be continued)