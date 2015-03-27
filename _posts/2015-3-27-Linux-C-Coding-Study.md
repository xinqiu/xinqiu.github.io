---
layout: post
title: Linux C 程序设计基础
description: "Linux C"
tags: [Linux,code]
image:
  background: geometry2.png
---

##Linux C 编程学习

> 这是我学习Linux C编程的笔记

##前期准备

---

###GCC相关


####gcc基本用法
	
{% highlight bash %}
~$ gcc [options][filenames]

{% endhighlight %}
######常用编译选项
 
 * -o : out_putfilename: 确定可执行文件的名称为output_filename，缺省则位a.out
 
 * -c : 只编译，不连接成为可执行文件，生成.o的文件
 
 * -g : 产生调试工具(GNU下是gdb)所必要的符号信息，想进行调试，必须加此选项
 
 * -O : 对程序进行优化编译、连接
 
 * -O2 : 比-O更好的优化编译，连接，编译、连接过程更慢
 
 * -Idirname : 将dirname所之处的目录添加到文件头文件目录列表中
  
 * -Ldirname : 讲dirname所指出的目录加入到库文件的目录列表中
 
 * -lname : 在连接是，装载名为`libname.a`的函数库
 
 * -statoc : 使用静态链接库文件,linux下连接的缺省操作是首先连接动态库
 
 * -Wall : 生成所有警告信息
 
 * -w : 不生成任何警告信息
 
 * -DMACRO : 定义MACRO宏，等效于在程序中使用#define MACRO
 
  
 > 运行是在终端里执行程序前加time可得到运行程序的时间情况
 
#####GDB程序调试

######1.启动GDB

{% highlight bash %}
~$ gdb filename
{% endhighlight %}

######2.在main函数处设置断点

{% highlight bash %}
(gdb) break main
{% endhighlight %}

######3.运行程序13

{% highlight bash %}
(gdb) run
{% endhighlight %}

######4.单步调试

{% highlight bash %}
(gdb) next
{% endhighlight %}

######.继续运行
{% highlight bash %}
(gdb) continue
{% endhighlight %}

#####GDB命令

* list(l) 查看程序
* break(b) 函数名 在函数入口添加断点
* break(b) 行号 在指定行添加断点
* break(b) 文件名:行号 指定文件指定行添加断点
* break(b) 行号if条件 当条件为真，指定行号处断点生效
* info break 查看所以设置的断点
* delete 断点编号 删除断点
* run(r) 开始运行程序
* next(n) 单步运行程序(不进入子函数)
* step(s) 单步运行程序(进入子函数)
* continue(c) 继续运行程序
* print(p) 变量名 查看变量的值
* finish 运行程序，知道当前函数结束
* watch 变量名 对指定变量进行监控
* quit(q) 退出gdb


####Makefile 工程管理

规则:

{% highlight bash %}
target:prerequisites
	command
{% endhighlight%}
注:命令需要以TAB键开始，第一条一般为最终目标

make命令默认在当前目录下寻找名字为makefile或者Makefile的工程文件，当名字不为这两者之一时，可以使用如下方法指定:

{% highlight bash %}
~$ make -f 文件名
{% endhighlight %}

Makefile中把那些没有任何依赖只有执行东子的目标称为"伪目标"(phony targets)

{% highlight bash %}
[例1]
.PHONY : clean
clean :
	rm -f hello main.o func1.o func2.o
注:.PHONY 将 clean 目标声明为伪目标 
[例2]
obj=main.o func1.o func2.o func3.o
hello:$(obj)
	gcc $(obj) -o hello
{% endhighlight %}

默认变量

* $^: 代表所有的依赖文件
* $@: 代表目标
* $<: 代表第一个依赖文件

其他Tips:

* `#` 后面的内容被视为注释

* @: 取消回显

---







