---
layout: post
title: Raspberry Pi 2 上手
description: "Raspberry Pi 2 "
tags: [raspberrypi]
date: 2015-7-26
---

> 家里的1代内存小，性能渣，所以入了新的2代。

<!--more-->
<!--toc-->

## 安装

### 下载OS

这里我使用的是`RASPBIAN`(2015-05-05).下载地址:http://www.raspberrypi.org/downloads 

### SD卡
这代用的是Micro SD，不知道会不会读写速度没SD卡好。
I
使用`SD Formatter`对卡进行格式化。格式化好后用`Win32 Disk Imager`将镜像拷入。一切准备OK后就可以接上电源开机了。

### SSH

首次启动会出现Raspi-config，当然之后也可以使用`sudo raspi-config`来更改系统设置。
第一件事是进入`8 Advanced Options`->`A4 SSH`,选择`Enable`.这样之后就可以直接在终端里用SSH连接树莓派了。

### 无线网卡
识别网卡后，要修改网络配置文件。修改`/etc/network/interfaces`文件。

使用命令

```bash
vi /etc/network/interfaces
```

## 一些工具

### 看门狗
树莓派的CPU是保护有硬件看门狗的，可以通过安装模块和值守程序来实现看门狗防止树莓派死机。

#### 安装方法
1.加载看门狗模块，编辑/etc/modules文件，添加一行“bcm2708_wdog”

```bash
sudo modprobe bcm2708_wdog
sudo vim /etc/modules
```

添加一行”bcm2708_wdog”


2.安装系统配置软件和看门狗程序

```bash
sudo apt-get install chkconfig watchdog
```

3.配置看门狗程序，编辑“/etc/watchdog.conf”文件

```bash
sudo vim /etc/watchdog.conf
```

去掉 watchdog-device = /dev/watchdog 前的#号，让看门狗设备对应树莓派的硬件看门狗
去掉 max-load-1 = 24 前的#号，当1分钟load进程超过24个的时候就会重启

还可以设置高温复位：
去掉
```bash
temperature-device =
max-temperature = 120
```
前的#号，改为

```bash
temperature-device = /sys/class/thermal/thermal_zone0/temp
max-temperature = 80000
```
温度超过80度就会引起重启，保护CPU。
配置完后，保存退出。

4.配置看门狗程序，开机自动运行

```bash
chkconfig watchdog on
```

5.启动看门狗

```bash
sudo /etc/init.d/watchdog start
```

### vsftpd


1,安装vsftpd服务器 (约400KB)

```bash
sudo apt-get install vsftpd
```

2,启动ftp服务

```bash
sudo service vsftpd start
```

3,编辑vsftdp的配置文件

```bash
sudo vim /etc/vsftpd.conf
```

找到以下行，定义一下

anonymous_enable=NO  

表示：不允许匿名访问

local_enable=YES   

设定本地用户可以访问。

write_enable=YES

设定可以进行写操作

local_umask=022

设定上传后文件的权限掩码。

存盘退出

4, 重启vsftpd服务

```bash
sudo service vsftpd restart
```

