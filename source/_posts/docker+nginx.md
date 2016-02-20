---
layout: post
title: 云主机下的docker+Nginx搭建
description: "docker Nginx "
tags: [docker,nginx]
date: 2015-11-13
---


> 之前申请到了腾讯云服务器，所以在上面折腾了一下 Nginx。

## 准备工作

### 系统配置

```html
操作系统	Ubuntu Server 14.04.1 LTS 64位
CPU	1核
内存	1GB
系统盘	8GB(本地盘)
数据盘	0GB
公网带宽	1Mbps
```

<!--more-->

### 系统镜像

一开始拿 Ubuntu 装 docker，结果启动后会出点小问题，所以就决定用腾讯云提供的系统镜像了。

```html

镜像名称	Docker运行环境（Ubuntu 14.04 64位）
类型	镜像市场镜像
镜像ID	img-3lj3495x
```

## docker 使用

用 ssh 连接主机，在终端里输入

```bash
docker -v
```

可以查看 docker 的版本，我这里的版本是`Docker version 1.8.2 build 0a8c2e3`

使用命令

```bash
docekr search nginx
```

可以搜索 nginx 仓库。

**注：如果发现 docker 使用会存在问题，可以使用 sudo -s 提权为 root**

使用官方的 nginx 仓库

```bash
docker pull nginx
```

pull 好以后，就可以正式启动 nginx 容器了。

官方的 nginx 容器里，连 vim 都没有，这是个比较苦恼的事情，所以可以先启动容器进入交互界面安装 vim。

```bash
docker run -t -i -p 80:80 nginx /bin/bash
```

这里进入的是 bash，`-p 80:80` 是将容器里的80端口与主机的80端口进行绑定。

进入容器后，会发现并不能访问容器里的 nginx 欢迎界面，这是因为 nginx 服务并没有启动。

使用命令

```bash
service nginx start
```

就可以启动 nginx 服务了。

为了安装 vim，首先需要使用命令更新源。

```bash
apt-get update
```

接着使用命令

```bash
apt-get install vim
```

中途敲 `y` 确定安装。

安装完以后就可以使用了。

## docker 常用命令

附加到一个已运行的容器

```bash
docker attach ID
```

停止一个容器

```bash
docker stop Name/ID
```

杀死一个容器

```bash
docker kill Name/ID
```

保存对容器的修改

```bash
docker commit ID new_image_name
```

列出当前所有正在运行的container

```bash
docker ps
```

列出所有container

```bash
docker ps -a
```

删除镜像

```bash
docker rmi image_name  
```

## Nginx 容器多域名绑定

在 docker Nginx 容器中，网站文件夹位于 `/usr/share/nginx`, 默认的欢迎页面在 `/usr/share/nginx/html` 中。

一般，如果域名绑定云服务器，那么访问域名访问的是 Nginx container 默认网站。如果先添加二级域名，访问同一个容器中的另一个网站，可以进行一下操作。

Nginx 的配置文件在 `/etc/nginx` 文件夹里。配置文件在 `conf.d` 文件夹里。`default.conf` 为默认网站的配置。添加站点在 `conf.d` 文件夹中，可以新建一个 `.conf` 文件，例如site1.conf：

```html
server {
    listen       80;
    server_name  此处填写你的二级域名;

    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;

    location / {
        root   /usr/share/nginx/about;
        index  index.html index.htm;
    }
}

```

如果这时候你就重启 nginx 服务，可能会启动失败，出现一下问题

```bash
could not build the server_names_hash, you should increase 
```

这是因为 `/etc/nginx/nginx.conf` 文件没有修改好。

```bash
vim /etc/nginx/nginx.conf
```

找到 `server_names_hash_max_size` 这行，将后面的数字改为 `512` ，将下一行的 `server_names_hash_bucket_size` 后面的数字改为 `128` 。

这时重启 Nginx 服务，就可以正常运行了。