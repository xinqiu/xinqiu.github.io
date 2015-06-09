---
layout: post
title: <<深入理解C指针>>读书笔记
description: "Understanding and Using C Pointers"
tags: [Notes]
image:
  background: photography.png
---

>指针可以说是C的灵魂，C语言入门很容易，但想精通，就必须要对指针有很透彻的理解。大一上学期学了一遍C语言，然而指针这个最重要的地方，却没有好好的深入研究。这本<<深入理解C指针>>虽然谈不上讲到多少指针的奇巧淫技，但最为复习指针的相关知识，开始可以稍微读读。

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
|1.pci is a variable|const int <strong>*pci</strong> | 
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

(To be continued)