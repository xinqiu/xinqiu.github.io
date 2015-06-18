---
layout: post
title: <<深入理解C指针>>读书笔记
description: "Understanding and Using C Pointers"
modified: 2015-6-18
tags: [Notes]
image:
  background: photography.png
---

>指针可以说是C的灵魂，C语言入门很容易，但想精通，就必须要对指针有很透彻的理解。大一上学期学了一遍C语言，然而指针这个最重要的地方，却没有好好的深入研究。这本<<深入理解C指针>>虽然谈不上讲到多少指针的奇巧淫技，但作为复习指针的相关知识，还是可以稍微读读。

## 阅读声明
倒过来读会让指针更容易理解。
￼￼￼
例如：

```
const int *pci;
```

---

| Explanation |  Declaration   |
| ------------- |:-------------:| 
|1.pci is a variable|const int *<strong>pci</strong> | 
|2.pci is a pointer variable| const int <strong> *pci</strong>| 
|3.pci is a pointer variable to an integer|const <strong> int *pci</strong> |
|4.pci is a pointer variable to a constant integer| <strong>const int *pci </strong>|
 
 ---
 
##常量与指针
 
和<<C专家编程>>一样，<<深入理解C指针>>也讲到了常量与指针。

###指向常量的指针

指针定义为指向常量，不能通过指针修改它所引用的值。

```
const int *ptr;
int const *ptr;
```

###指向非常量的常量指针

指针不可变，但所指向的数据可变。指针必须被初始化为指向非常量变量。

```
int *const ptr;
```

###指向常量的常量指针
 
指针本身不能修改，指向的数据也不能通过它来修改。

```
const int *const ptr;
```

###指向『指向常量的常量指针』的指针

```
const int * const * ptr;
```

##动态内存分配

* malloc
* realloc
* calloc

| Function |  Declaration   |
| ------------- |:-------------:| 
|malloc|从堆上分配内存| 
|realloc|在之前分配的内存块基础上，将内存重新分配为更大或者更小的部分|
|calloc|从堆上分配内存并清零|  

###变长数组

使用alloca函数(微软为malloca)在函数的栈帧上分配内存。函数返回后自动释放内存。

####栈帧
栈帧由以下几种元素组成

* 返回地址
* 局部数据存储
* 参数存储
* 栈指针和基指针

##动态分配二维数组
###动态分配可能不连续的内存

以下代码演示了如何创建一个内存可能不连续的二维数组。

{% highlight c %}
int rows = 2;
int columns = 5;

int **matrix = (int **) malloc(rows * sizeof(int *));

for(int i = 0; i < rows; i++){
	matrix[i] = (int *) malloc(columns * sizeof(int))
}
{% endhighlight %}

###动态分配连续内存

{% highlight c %}
int rows = 2;
int columns = 5;

int **matrix = (int **) malloc(rows * sizeof(int *));
matrix[0] = (int *) malloc(rows * columns * sizeof(int));
for(int i = 0; i < rows; i++){
	matrix[i] = matrix[0] + i * columns;
}
{% endhighlight %}
以上代码演示了第一种技术，第一个malloc分配了一个整数指针数组，一个元素用来存储一行的指针。第二个malloc在存储每行第一个元素的地址。

第二种技术是一次性分配数组所需的所有内存。
{% highlight c %}
int *matrix = (int *) malloc(rows * columns * sizeof(int));
{% endhighlight %}

##结构体内存大小

为结构体分配内存时，分配的内存至少是各个字段的长度和。实际长度通常大于这个和。某些数据类型需要对齐到特定边界。比如说，短整数通常对齐到能被2整除的地址上，而整数对齐到能被4整除的地址上。

##避免malloc/free开销

重复分配然后释放结构体会尝试一些开销，可能导致巨大的性能瓶颈。解决这问题的一种办法是为分配的结构体单独维护一个表。当用户不再需要某个结构体实例时，将其返回结构体池中。当需要某个实例，则从结构体池中获取一个对象。如果没有可用的元素，就动态分配一个实例。但表的长度则成为了一个问题。但这个问题是可以解决。

##处理未初始化指针

有三种方法可以用来处理未初始化的指针:

* 总是用NULL来初始化指针
* 用assert函数
* 用第三方工具

assert函数判断表达式是否为真，表达式为假，程序会终止。

##函数指针

###声明函数指针

{% highlight c %}
void (*foo)();
{% endhighlight %}
foo为函数指针。要注意的是，如果声明是

{% highlight c %}
int *foo();
{% endhighlight %}
意义就变了，代表foo函数返回一个int型指针。

为函数指针声明一个类型定义会比较方便，但类型定义看起来有点奇怪，通常，类型定义的名字是声明的最后一个元素。

{% highlight c %}
typedef int (*funcptr)(int);
{% endhighlight %}

举个栗子

{% highlight c %}
typedef int (*funcptr)(int);
funcptr fptr2;
fptr2 = foo; // 	foo为函数名
fptr(n);	// 调用foo函数
{% endhighlight %}
### 传递函数指针

只要把函数指针声明最为函数参数即可。

举个栗子

{% highlight c %}
int add(int num1, int num2){
	return num1 + num2;
}

int substract(int num1, int num2){
	return num1 - num2;
}

typedef int (*fptrOperation)(int, int);

int compute(fptrOperation operation, int num1, int num2){
	return operation(num1, num2);
}
{% endhighlight %}

###返回函数指针
返回函数指针需要把函数的返回类型声明为函数指针。

接着上一个的例子

{% highlight c %}
fptrOperation select(char opcode){
    switch(opcode){
        case '+': return add;
        case '-': return substract;
    }
    return 0;
}
// evaluate函数整合了其他函数。该函数接受两个整数和一个字符，
// 字符代表要做的操作，它会把opcode传递给select函数，
// 后者返回要执行的函数指针。
int evaluate(char opcode, int num1, int num2)
{
    fptrOperation operation = select(opcode);
    return operation(num1, num2);
}
{% endhighlight %}

###函数指针数组

把函数指针声明为数组的类型。
接着上面的例子

{% highlight c %}
typedef int (*opertation)(int, int);
operation operations[128] = {NULL};
// 或者 int(*operations[128])(int, int) = {NULL};
// 用指针数组来避免使用switch
void initializeOperationsArray(){
	operations['+'] = add;
	operations['-'] = subtract;
}
// 所以evaluate需要改写为evaluateArray.
int evaluateArray(char opcode, int num1, int num2){
	fptrOperation operation;
	operation = operations[opcode];
	return operation(num1, num2);
}
{% endhighlight %}

##指针安全方面

###清除敏感数据

复写敏感数据可以使用`memset`函数。

##其他重要内容

* 指针的类型转换
* 访问硬件设备
* 别名和强别名
* 使用restrict关键字
* 线程
* 面向对象技术

书中最后的部分简单的提及了一些高级技巧，这块知识，我觉得还是看其他详细的书比较好。

