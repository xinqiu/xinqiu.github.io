---
layout: post
title: Python科学计算学习
description: "NumPy, SciPy, Matplotlib"
tags: [python]
image:
  background: photography.png
---

> 之前参加数学建模比赛都是用的 MatLab，然而电脑每次运行 MatLab 都烫的要命，所以决定用自己比较熟悉的 python 来进行科学计算。

##NumPy

NumPy提供了两种基本的对象：ndarray（N-dimensional array object）和 ufunc（universal function object）。ndarray(下文统一称之为数组)是存储单一数据类型的多维数组，而ufunc则是能够对数组进行处理的函数。

推荐使用以下方法导入NumPy 函数库：

{% highlight python %}
import numpy as np
{% endhighlight %}

###ndarray对象

####创建

通过给array函数传递Python的序列对象创建数组，如果传递的是多层嵌套的序列，将创建多维数组：

{% highlight python %}
>>> A = np.array([1,2,3,4])
>>> A
array([1, 2, 3, 4])
>>> B = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
>>> B
array([[ 1,  2,  3,  4],
       [ 4,  5,  6,  7],
       [ 7,  8,  9, 10]])
>>>
{% endhighlight %}

上面的例子是在 python 交互界面中产生的结果，在 PyCharm 中运行以下代码:

{% highlight python %}
import numpy as np

A = np.array([1,2,3,4])
B = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])

print A
print B
{% endhighlight %}

显示的是：

{% highlight python %}
[1 2 3 4]
[[ 1  2  3  4]
 [ 4  5  6  7]
 [ 7  8  9 10]]
{% endhighlight %}

数组的shape属性返回的是数组的维度的 Tuple 。如果是以为数组，就省略了维度1，直接显示元素个数，如果是二维数组，返回的 Tuple 第一个元素代表二维数组是几行，第二个元素代表二维数组是几列。多维数组亦可以表示。

{% highlight python %}
>>> A.shape
(4,)
>>> B.shape
(3, 4)
>>>
{% endhighlight %}

还可以使用数组的 reshape 方法，创建一个改变了尺寸的新数组。

{% highlight python %}
>>> C = A.reshape((2,2))
>>> C
array([[1, 2],
       [3, 4]])
>>> 
{% endhighlight %}

数组的 dtype 属性代表数组的元素类型，可以在创建数组的时候，使用 dtype 参数来改变元素类型。`float`代表浮点数，`complex`代表复数。

{% highlight python %}
>>> np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.complex)
array([[  1.+0.j,   2.+0.j,   3.+0.j,   4.+0.j],
       [  4.+0.j,   5.+0.j,   6.+0.j,   7.+0.j],
       [  7.+0.j,   8.+0.j,   9.+0.j,  10.+0.j]])
>>> 
{% endhighlight %}

NumPy提供了很多专门用来创建数组的函数。

* arange 函数类似于python的range函数，通过指定开始值、终值和步长来创建一维数组，注意数组不包括终值:

	{% highlight python %}
	>>> np.arange(0,1,0.1)
array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
	{% endhighlight %}
	
* linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值:

	{% highlight python %}
 np.linspace(0, 1, 12)
array([ 0.        ,  0.09090909,  0.18181818,  0.27272727,  0.36363636,
        0.45454545,  0.54545455,  0.63636364,  0.72727273,  0.81818182,
        0.90909091,  1.        ])
	{% endhighlight %}

* logspace函数和linspace类似，不过它创建等比数列，下面的例子产生1(10^0)到100(10^2)、有20个元素的等比数列:

	{% highlight python %}
	>>> np.logspace(0, 2, 20)
array([   1.        ,    1.27427499,    1.62377674,    2.06913808,
          2.6366509 ,    3.35981829,    4.2813324 ,    5.45559478,
          6.95192796,    8.8586679 ,   11.28837892,   14.38449888,
         18.32980711,   23.35721469,   29.76351442,   37.92690191,
         48.32930239,   61.58482111,   78.47599704,  100.        ])
	{% endhighlight %}

###ufunc运算

ufunc 是 universal function 的缩写，它是一种能对数组的每个元素进行操作的函数。

frompyfunc 是将任意的 Python 函数转为 Numpy ufunc。frompyfunc 的调用格式为 frompyfunc(func, nin, nout)，其中 func 是计算单个元素的函数，nin 是此函数的输入参数的个数，nout 是此函数的返回值的个数。

reduce 方法和Python的reduce函数类似。

###矩阵运算

使用matrix类创建的是矩阵对象，它们的加减乘除运算缺省采用矩阵方式计算，用法和matlab十分类似。

* dot : 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；对于二维数组，计算的是两个数组的矩阵乘积；对于多维数组，它的通用计算公式如下，即结果数组中的每个元素都是：数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和：

	{% highlight python %}
	dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
	{% endhighlight %}
	
* inner : 和dot乘积一样，对于两个一维数组，计算的是这两个数组对应下标元素的乘积和；对于多维数组，它计算的结果数组中的每个元素都是：数组a和b的最后一维的内积，因此数组a和b的最后一维的长度必须相同：

	{% highlight python %}
	inner(a, b)[i,j,k,m] = sum(a[i,j,:]*b[k,m,:])
	{% endhighlight %}
	
* outer : 只按照一维数组进行计算，如果传入参数是多维数组，则先将此数组展平为一维数组之后再进行运算。outer乘积计算的列向量和行向量的矩阵乘积。



