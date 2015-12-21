---
layout: post
title: Flask补坑记录
description: "Flask"
tags: [python]
image:
  background: photography.png
---

##前言
不得不说，Flask是个不错的框架，它很简洁，然而却不失强大。在我阅读<<Flask Web Development>>这本书的过程中，我觉得最好是这本书的配套源码和issues。在这些帮助下，一步步从完全不了解Flask到稍微知道Flask的工作原理。这过程中有好多次因为一些小细节的错误debug个很久。在此，我记录了一些我遇到的问题，方便大家看看。


##数据库
###迁移相关问题
Flask提供了一个库Flask-SQLAlchemy。这个库大大的简化了数据库的操作，不需要手写数据库语句。配合数据库迁移的库Flask-Migrate,功能会非常强大。然而，在我尝试迁移数据库的时候，经常出现一个现象。

{% highlight bash %}
python manager.py db upgrade

INFO  [alembic.migration] Context impl SQLiteImpl.
INFO  [alembic.migration] Will assume non-transactional DDL.
{% endhighlight %}

总之就是并没有迁移成功。

后来发现, 如果在`upgrade`之前`migrate`一下就可以解决问题了。

###权限问题

因为学习Flask是断断续续的，不可避免的就是遇到问题要不停的回滚。结果就是对数据库的操作存在一些隐形问题。在做到11章时，一个问题浮现了出来，就是登陆以后的用户并不能发post。在代码审计了很久都没有发现问题的时候，无意间看到了一个issue，和我遇到了一样的问题。原因是因为Role角色没写进数据库中，所以注册的用户并没有权限。

{% highlight bash %}
python manage.py shell
>>> Role.insert_roles()
>>> Role.query.all() #应该能看到下面的三种角色
[<Role u'Administrator'>, <Role u'User'>, <Role u'Moderator'>]
{% endhighlight %}

当初觉得这个很麻烦，在书的后面，给出了解决方法，就是在部署的时候，直接执行insert_roles()，省去了Shell里的这一步。

##邮件

邮件操作让我折腾了一两天，换了163，126，qq。刚才是都没成功。错误代码`530，Authentication Required.`明明邮箱密码并没有输错呀。后来仔细想了想，发现不管是QQ还是网易，在使用第三方Mail接收客户端的时候，使用的密码并不是邮箱密码，而是一个授权码。在使用授权码成功发送了一篇邮件以后，心里顿时舒坦多了，也预示着Flask小网站完成了一大半了。

##一些知识点的记录
###url_for

因为Flask使用的是`jinja2`模板, 其中网页跳转使用了url_for函数。当初在学Blueprint的时候并没细细思考蓝图的一些原理，当初用url_for也没怎么注意。在某个瞬间，突然发现url_for有的时候用了`.`，有时却没用。这是为什么呢？

{% highlight text %}
Additionally if you are in a view function of a blueprint or
 a rendered template and you want to link to another endpoint of the same blueprint, you can use relative redirects by 
 prefixing the endpoint with a dot only
{% endhighlight %}

简而言之就是，这里的点其实省略了当前蓝图的名字。


##总结

Flask真心不错，很适合学完了Python，却又不知道该拿python去做个什么简单的项目。打算之后做个Flask博客试试，到时候再继续补坑。最近突然想刷算法题目了233.