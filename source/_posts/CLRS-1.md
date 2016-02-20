---
layout: post
title: 算法导论第2章算法基础练习
description: "CLRS"
tags: [algorithm]
date: 2015-8-31
---

<!-- toc -->

#### 2.1-1

Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array `A = <31, 41, 59, 26, 41, 58>`.

<!-- more -->
![](CLRS-1.1.png)

#### 2.1-2

Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of non-decreasing order.

```python
INSERTION-SORT(A)
for j = 2 to A.length
	key = A[j]􏰀
	// Insert A[j] into the sorted sequence A[1..j - 1].
	i = j - 1
	while i > 0 and A[i] < key
		A[i + 1] = A[i]
		i = i - 1
	A[i + 1] = key
```

#### 2.1-3

Consider the searching problem:

**Input**: A sequence of n numbers A = <a1, a2, ..., an> and a value *v*.

**Output**: An index i such that *v* = A[i] or the special value NIL if *v* does not appear in A.

```python
LINEAR-SEARCH(A , v)
for i = 1 to n
	if A[i] = v
		return i
	i = i + 1

return NIL
```

#### 2.1-4

Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n + 1)-element array C . State the problem formally and write pseudocode for adding the two integers.

```python
SUM(A, B, C)
// 此处假设C元素全部初始化为0
for i = n to 1
	C[n + 1] = A[i] + B[i]
	if C[n + 1] > 2
		C[n + 1] = C[n + 1] - 2
		C[n] = C[n] + 1

```

#### 2.2-1

Express the function ![](http://www.zhihu.com/equation?tex=n%5E3)/1000 - 100![](http://www.zhihu.com/equation?tex=n%5E2) - 1000n + 3 in terms of Θ-notation.

Θ(![](http://www.zhihu.com/equation?tex=n%5E3))

#### 2.2-2

Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1]. Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n - 1 elements of A. Write pseudocode for this algorithm, which is known as *selection sort*. What loop invariant does this algorithm maintain? Why does it need to run for only the first n - 1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in Θ-notation.

```python
SELECTION-SORT(A)
for i = 1 to n - 1
	key = A[i]
	index = i
	for j = i + 1 to n
		if A[i] < key
			key = A[i]
			index = j
	A[index] = A[i]
	A[i] = key
```
循环不变式就不写了
最好最坏情况都是Θ(![](http://www.zhihu.com/equation?tex=n%5E2))

#### 2.2-3

Consider linear search again (see Exercise 2.1-3). How many elements of the in- put sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear search in Θ-notation? Justify your answers.

最坏的情况为n,平均和最坏情况运行时间都为Θ(n).

#### 2.2-4

How can we modify almost any algorithm to have a good best-case running time?

分析问题，运用数学知识不断推导得出最优解？这题。。。

#### 2.3-1

Using Figure 2.4 as a model, illustrate the operation of merge sort on the array A = <3, 41, 52, 26, 38, 57, 9, 49>. 

![](CLRS-1.2.png)

#### 2.3-2

Rewrite the MERGE procedure so that it does not use sentinels, instead stopping once either array L or R has had all its elements copied back to A and then copying the remainder of the other array back into A.

```python
// 已知LR已排序
n1 = q - p + 1
n2 = r - p

MERGE(A,p,q,r)

	for i = 1 to n1
		L[i] = A[p + i - 1]
	for j = 1 to A[q + j]
		R[j] = A[q+j]

	for k = p to r
		 if i < n1 and j < n2
		 	if L[i] <= R[j]
		 		A[k] = L[i]
		 		i = i + 1
		 		continue
			else A[k] = R[j]
				j = j + 1
				continue

		if i > =n1 and j < n2:
			A[k] = R[j]
			j = j + 1
			continue
		if i < n1 and j > n2
			A[k] = L[i]
			i = i + 1
			continue

```
