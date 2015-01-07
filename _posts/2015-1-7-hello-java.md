---
layout: post
title: Hello Java
description: "hello Java"
tags: [sample post,code,Java]
image:
  feature: abstract-3.jpg
---

##IntelliJ IDEA Java入门

首先申明下，我是纯新手，没有Java开发经验，本来想用Eclipse，介于网上普遍说IntelliJ IDEA是最好的Java IDE，于是从Eclipse转IntelliJ IDEA。网上关于新建普通的Hello World的Java程序的介绍很少，只好自己捣鼓。

####IntelliJ IDEA 14

* `File`->`New Project`->`Empty Project`->`Next`->改Project name/location->`Finish`

* `File`->`New Maven`->`Next`->改ArtifactId->改Project name/location->`Finish`

* 左边Project列表下进入`src`->`main`->`java`,右击`java`点New，创建`Package`，再右击`Package`，点New创建`Java Class`


在Class{}里添加

{% highlight java %}
public static void main(String[] args){
        System.out.println("Hello World\nHello Java\n");
    }
{% endhighlight %}
就能实现Hello World的Java程序了