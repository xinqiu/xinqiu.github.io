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

## SciPy

SciPy函数库在NumPy库的基础上增加了众多的数学、科学以及工程计算中常用的库函数。例如线性代数、常微分方程数值求解、信号处理、图像处理、稀疏矩阵等等。由于其涉及的领域众多、本书没有能力对其一一的进行介绍。作为入门介绍，让我们看看如何用SciPy进行插值处理、信号滤波以及用C语言加速计算。

###最小二乘拟合

今年的数学建模国赛——太阳影子长度中，就有一问需要用到最小二乘法拟合，可惜当初不是很会。最小二乘法就是假设有一组实验数据(x[i], y[i])，我们知道它们之间的函数关系:y = f(x)，通过这些已知信息，需要确定函数中的一些参数项。例如，如果f是一个线型函数f(x) = k*x+b，那么参数k和b就是我们需要确定的值。如果将这些参数用 p 表示的话，那么我们就是要找到一组 p 值使得如下公式中的S函数最小:

![](http://www.zhihu.com/equation?tex=S(p\)=\sum_{i=1}^m[y_{i}-f(x_{i},P\)]^{2})
这种算法被称之为最小二乘拟合(Least-square fitting)。

scipy中的子函数库optimize已经提供了实现最小二乘拟合算法的函数leastsq。下面是用leastsq进行数据拟合的一个例子：

{% highlight python %}
# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)   

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6 # 真实数据的函数参数
y0 = func(x, [A, k, theta]) # 真实数据
y1 = y0 + 2 * np.random.randn(len(x)) # 加入噪声之后的实验数据    

p0 = [7, 0.2, 0] # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y1, x))

print u"真实参数:", [A, k, theta] 
print u"拟合参数", plsq[0] # 实验数据拟合后的参数

pl.plot(x, y0, label=u"真实数据")
pl.plot(x, y1, label=u"带噪声的实验数据")
pl.plot(x, func(x, plsq[0]), label=u"拟合数据")
pl.legend()
pl.show()
{% endhighlight %}

通过leastsq函数对带噪声的实验数据x, y1进行数据拟合，可以找到x和真实数据y0之间的正弦关系的三个参数： A, k, theta。

### 函数最小值

optimize库提供了几个求函数最小值的算法：fmin, fmin_powell, fmin_cg, fmin_bfgs。就只举一个小例子：

{% highlight python %}
from scipy.optimize import fmin
def myfunc（x）：
    return x**2-4*x+8
x0=[2]
xopt=fmin(myfunc,x0)
print xopt
{% endhighlight %}

返回结果：

{% highlight python %}
Optimization terminated successfully.
         Current function value: 4.000000
         Iterations: 11
         Function evaluations: 22
[ 2.]
{% endhighlight %}

其中 x0 为 初始估计值。




##参考资料

[用Python做科学计算](http://old.sebug.net/paper/books/scipydoc/index.html)

[Numpy and Scipy Documentation](http://docs.scipy.org/doc/)

