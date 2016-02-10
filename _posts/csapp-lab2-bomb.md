---
layout: post
title: CSAPP Lab2 解题分析
description: "csapp"
tags: [csapp]
image:
  background: ps_neutral.png
---

Lab2 的 Bomb是个非常有意思的实验，比起之前耗脑的Lab1，这个Lab主要是学习反汇编。

这里我的环境是OS X EI Capitan，Lab2是[Updated 1/12/16].

##Phase1

在Mac上是默认没有GDB的，可以使用LLDB来代替。

进入lldb

{% highlight bash %}
lldb bomb
{% endhighlight %}

使用`disassemble`进行反汇编,参考`bomb.c`文件，可以知道主要的几个函数名。

首先是Phase_1

{% highlight bash %}
(lldb) disas -n phase_1
{% endhighlight %}

得到以下汇编代码

{% highlight c-objdump %}
bomb`phase_1:
bomb[0x400ee0] <+0>:  subq   $0x8, %rsp
bomb[0x400ee4] <+4>:  movl   $0x402400, %esi
bomb[0x400ee9] <+9>:  callq  0x401338                  ; strings_not_equal
bomb[0x400eee] <+14>: testl  %eax, %eax
bomb[0x400ef0] <+16>: je     0x400ef7                  ; <+23>
bomb[0x400ef2] <+18>: callq  0x40143a                  ; explode_bomb
bomb[0x400ef7] <+23>: addq   $0x8, %rsp
bomb[0x400efb] <+27>: retq  
{% endhighlight %}

这段代码还是挺好理解的，保存`Stack pointer`,将`$0x402400`传给`%esi`,调用位于`0x401338`的`strings_not_equal`函数，比较`%eax`是否为0，不为零则调用`explode_bomb`函数，为零则返回。

所以关键要找出字符串是什么。根据上述的汇编代码，可以发现字符串被保存在`0x402400`这个内存里，所以使用`x/s`来查看。

{% highlight c-objdump %}
(lldb) x/s 0x402400
{% endhighlight %}

得到

{% highlight c-objdump %}
0x00402400: "Border relations with Canada have never been better."
{% endhighlight %}

所以第一关的答案是`Strings_Not_Equal`

##Phase2

同样，还是先反汇编出代码

{% highlight c-objdump %}
bomb`phase_2:
bomb[0x400efc] <+0>:  pushq  %rbp
bomb[0x400efd] <+1>:  pushq  %rbx
bomb[0x400efe] <+2>:  subq   $0x28, %rsp
bomb[0x400f02] <+6>:  movq   %rsp, %rsi
bomb[0x400f05] <+9>:  callq  0x40145c                  ; read_six_numbers
bomb[0x400f0a] <+14>: cmpl   $0x1, (%rsp)
bomb[0x400f0e] <+18>: je     0x400f30                  ; <+52>
bomb[0x400f10] <+20>: callq  0x40143a                  ; explode_bomb
bomb[0x400f15] <+25>: jmp    0x400f30                  ; <+52>
bomb[0x400f17] <+27>: movl   -0x4(%rbx), %eax
bomb[0x400f1a] <+30>: addl   %eax, %eax
bomb[0x400f1c] <+32>: cmpl   %eax, (%rbx)
bomb[0x400f1e] <+34>: je     0x400f25                  ; <+41>
bomb[0x400f20] <+36>: callq  0x40143a                  ; explode_bomb
bomb[0x400f25] <+41>: addq   $0x4, %rbx
bomb[0x400f29] <+45>: cmpq   %rbp, %rbx
bomb[0x400f2c] <+48>: jne    0x400f17                  ; <+27>
bomb[0x400f2e] <+50>: jmp    0x400f3c                  ; <+64>
bomb[0x400f30] <+52>: leaq   0x4(%rsp), %rbx
bomb[0x400f35] <+57>: leaq   0x18(%rsp), %rbp
bomb[0x400f3a] <+62>: jmp    0x400f17                  ; <+27>
bomb[0x400f3c] <+64>: addq   $0x28, %rsp
bomb[0x400f40] <+68>: popq   %rbx
bomb[0x400f41] <+69>: popq   %rbp
bomb[0x400f42] <+70>: retq   
{% endhighlight %}

从上述汇编中，可以发现从%rsp位置开始保存数字。

反汇编`read_six_numbers`得到

{% highlight c-objdump %}
bomb`read_six_numbers:
bomb[0x40145c] <+0>:  subq   $0x18, %rsp
bomb[0x401460] <+4>:  movq   %rsi, %rdx
bomb[0x401463] <+7>:  leaq   0x4(%rsi), %rcx
bomb[0x401467] <+11>: leaq   0x14(%rsi), %rax
bomb[0x40146b] <+15>: movq   %rax, 0x8(%rsp)
bomb[0x401470] <+20>: leaq   0x10(%rsi), %rax
bomb[0x401474] <+24>: movq   %rax, (%rsp)
bomb[0x401478] <+28>: leaq   0xc(%rsi), %r9
bomb[0x40147c] <+32>: leaq   0x8(%rsi), %r8
bomb[0x401480] <+36>: movl   $0x4025c3, %esi
bomb[0x401485] <+41>: movl   $0x0, %eax
bomb[0x40148a] <+46>: callq  0x400bf0                  ; symbol stub for: __isoc99_sscanf
bomb[0x40148f] <+51>: cmpl   $0x5, %eax
bomb[0x401492] <+54>: jg     0x401499                  ; <+61>
bomb[0x401494] <+56>: callq  0x40143a                  ; explode_bomb
bomb[0x401499] <+61>: addq   $0x18, %rsp
bomb[0x40149d] <+65>: retq 
{% endhighlight %}

根据Phase1,很敏感的会发现`movl   $0x4025c3, %esi`这行。通过之前一样的方法，得到`0x4025c3`内存里的字符串，

{% highlight c-objdump %}
0x004025c3: "%d %d %d %d %d %d"
{% endhighlight %}

再根据`bomb[0x40148a] <+46>: callq  0x400bf0                  ; symbol stub for: __isoc99_sscanf`这句，猜一下，立马就能联想到`scanf("%d %d %d %d %d %d",a,b,c,d,e,f);`，也就是说，输入的格式已经确定了。

`bomb[0x40145c] <+0>:  subq   $0x18, %rsp`这行也暗示了之前`bomb[0x400f35] <+57>: leaq   0x18(%rsp), %rbp`为什么是0x18(%rsp)。

回到`phase_2`，根据`cmpl   $0x1, (%rsp)`和下一行汇编语句，很容易知道第一个数是1.
接着跳到了`<+52>`,将0x4(%rsp)指向内存里的值传给%rbx,将0x18(%rsp)指向内存里的值传给%rbp。

{% highlight c-objdump %}
bomb[0x400f17] <+27>: movl   -0x4(%rbx), %eax
bomb[0x400f1a] <+30>: addl   %eax, %eax
bomb[0x400f1c] <+32>: cmpl   %eax, (%rbx)
bomb[0x400f1e] <+34>: je     0x400f25  
{% endhighlight %}

这段代码是循环里的部分

{% highlight c-objdump %}
bomb[0x400f25] <+41>: addq   $0x4, %rbx
bomb[0x400f29] <+45>: cmpq   %rbp, %rbx
bomb[0x400f2c] <+48>: jne    0x400f17                  ; <+27>
bomb[0x400f2e] <+50>: jmp    0x400f3c                  ; <+64>
{% endhighlight %}

这是循环条件

所以可以得出这6个数是等比数列`1 2 4 8 16 32`

##Phase3

{% highlight c-objdump %}
bomb`phase_3:
bomb[0x400f43] <+0>:   subq   $0x18, %rsp
bomb[0x400f47] <+4>:   leaq   0xc(%rsp), %rcx
bomb[0x400f4c] <+9>:   leaq   0x8(%rsp), %rdx
bomb[0x400f51] <+14>:  movl   $0x4025cf, %esi
bomb[0x400f56] <+19>:  movl   $0x0, %eax
bomb[0x400f5b] <+24>:  callq  0x400bf0                  ; symbol stub for: __isoc99_sscanf
bomb[0x400f60] <+29>:  cmpl   $0x1, %eax
bomb[0x400f63] <+32>:  jg     0x400f6a                  ; <+39>
bomb[0x400f65] <+34>:  callq  0x40143a                  ; explode_bomb
bomb[0x400f6a] <+39>:  cmpl   $0x7, 0x8(%rsp)
bomb[0x400f6f] <+44>:  ja     0x400fad                  ; <+106>
bomb[0x400f71] <+46>:  movl   0x8(%rsp), %eax
bomb[0x400f75] <+50>:  jmpq   *0x402470(,%rax,8)
bomb[0x400f7c] <+57>:  movl   $0xcf, %eax
bomb[0x400f81] <+62>:  jmp    0x400fbe                  ; <+123>
bomb[0x400f83] <+64>:  movl   $0x2c3, %eax
bomb[0x400f88] <+69>:  jmp    0x400fbe                  ; <+123>
bomb[0x400f8a] <+71>:  movl   $0x100, %eax
bomb[0x400f8f] <+76>:  jmp    0x400fbe                  ; <+123>
bomb[0x400f91] <+78>:  movl   $0x185, %eax
bomb[0x400f96] <+83>:  jmp    0x400fbe                  ; <+123>
bomb[0x400f98] <+85>:  movl   $0xce, %eax
bomb[0x400f9d] <+90>:  jmp    0x400fbe                  ; <+123>
bomb[0x400f9f] <+92>:  movl   $0x2aa, %eax
bomb[0x400fa4] <+97>:  jmp    0x400fbe                  ; <+123>
bomb[0x400fa6] <+99>:  movl   $0x147, %eax
bomb[0x400fab] <+104>: jmp    0x400fbe                  ; <+123>
bomb[0x400fad] <+106>: callq  0x40143a                  ; explode_bomb
bomb[0x400fb2] <+111>: movl   $0x0, %eax
bomb[0x400fb7] <+116>: jmp    0x400fbe                  ; <+123>
bomb[0x400fb9] <+118>: movl   $0x137, %eax
bomb[0x400fbe] <+123>: cmpl   0xc(%rsp), %eax
bomb[0x400fc2] <+127>: je     0x400fc9                  ; <+134>
bomb[0x400fc4] <+129>: callq  0x40143a                  ; explode_bomb
bomb[0x400fc9] <+134>: addq   $0x18, %rsp
bomb[0x400fcd] <+138>: retq 
{% endhighlight %}
代码还挺长。

同样，根据`bomb[0x400f51] <+14>:  movl   $0x4025cf, %esi`可以得到`%d %d`这个格式，代表要输入两个整数。

{% highlight c-objdump %}
bomb[0x400f47] <+4>:   leaq   0xc(%rsp), %rcx
bomb[0x400f4c] <+9>:   leaq   0x8(%rsp), %rdx
{% endhighlight %}

这两行代表了两个数存的位置。

{% highlight c-objdump %}
bomb[0x400f6a] <+39>:  cmpl   $0x7, 0x8(%rsp)
bomb[0x400f6f] <+44>:  ja     0x400fad                  ; <+106>
{% endhighlight %}

由这两行，可知第一个数要不能大于7,`ja`是`unsigned >`，所以第一个数还要是正数。

关键的一行是这个`bomb[0x400f75] <+50>:  jmpq   *0x402470(,%rax,8)`,这是一个switch跳转语句，跳转到`0x402470+ %rax * 8`的位置。使用`p/x`来确定跳转的目的地址。

{% highlight c-objdump %}
(gdb) p/x *(0x402470)$1 = 0x400f7c(gdb) p/x *(0x402470+8)$2 = 0x400fb9(gdb) p/x *(0x402470+16)$3 = 0x400f83(gdb) p/x *(0x402470+24)$4 = 0x400f8a(gdb) p/x *(0x402470+32)$5 = 0x400f91(gdb) p/x *(0x402470+40)$6 = 0x400f98(gdb) p/x *(0x402470+48)$7 = 0x400f9f(gdb) p/x *(0x402470+56)$8 = 0x400fa6
{% endhighlight %}

通过这个跳转表，可得得到8个解

{% highlight text %}
0 207
1 311
2 707
3 256
4 389
5 206
6 682
7 327
{% endhighlight %}

##Phase4

{% highlight c-objdump %}
bomb`phase_4:
bomb[0x40100c] <+0>:  subq   $0x18, %rsp
bomb[0x401010] <+4>:  leaq   0xc(%rsp), %rcx
bomb[0x401015] <+9>:  leaq   0x8(%rsp), %rdx
bomb[0x40101a] <+14>: movl   $0x4025cf, %esi
bomb[0x40101f] <+19>: movl   $0x0, %eax
bomb[0x401024] <+24>: callq  0x400bf0                  ; symbol stub for: __isoc99_sscanf
bomb[0x401029] <+29>: cmpl   $0x2, %eax
bomb[0x40102c] <+32>: jne    0x401035                  ; <+41>
bomb[0x40102e] <+34>: cmpl   $0xe, 0x8(%rsp)
bomb[0x401033] <+39>: jbe    0x40103a                  ; <+46>
bomb[0x401035] <+41>: callq  0x40143a                  ; explode_bomb
bomb[0x40103a] <+46>: movl   $0xe, %edx
bomb[0x40103f] <+51>: movl   $0x0, %esi
bomb[0x401044] <+56>: movl   0x8(%rsp), %edi
bomb[0x401048] <+60>: callq  0x400fce                  ; func4
bomb[0x40104d] <+65>: testl  %eax, %eax
bomb[0x40104f] <+67>: jne    0x401058                  ; <+76>
bomb[0x401051] <+69>: cmpl   $0x0, 0xc(%rsp)
bomb[0x401056] <+74>: je     0x40105d                  ; <+81>
bomb[0x401058] <+76>: callq  0x40143a                  ; explode_bomb
bomb[0x40105d] <+81>: addq   $0x18, %rsp
bomb[0x401061] <+85>: retq
{% endhighlight %}

同样的方式，可以确定第一个整数小于等于14，第二个数为0。

第一个数具体值，需要执行func4。

所以func4的代码

{% highlight c-objdump %}
bomb`func4:
bomb[0x400fce] <+0>:  subq   $0x8, %rsp
bomb[0x400fd2] <+4>:  movl   %edx, %eax
bomb[0x400fd4] <+6>:  subl   %esi, %eax
bomb[0x400fd6] <+8>:  movl   %eax, %ecx
bomb[0x400fd8] <+10>: shrl   $0x1f, %ecx
bomb[0x400fdb] <+13>: addl   %ecx, %eax
bomb[0x400fdd] <+15>: sarl   %eax
bomb[0x400fdf] <+17>: leal   (%rax,%rsi), %ecx
bomb[0x400fe2] <+20>: cmpl   %edi, %ecx
bomb[0x400fe4] <+22>: jle    0x400ff2                  ; <+36>
bomb[0x400fe6] <+24>: leal   -0x1(%rcx), %edx
bomb[0x400fe9] <+27>: callq  0x400fce                  ; <+0>
bomb[0x400fee] <+32>: addl   %eax, %eax
bomb[0x400ff0] <+34>: jmp    0x401007                  ; <+57>
bomb[0x400ff2] <+36>: movl   $0x0, %eax
bomb[0x400ff7] <+41>: cmpl   %edi, %ecx
bomb[0x400ff9] <+43>: jge    0x401007                  ; <+57>
bomb[0x400ffb] <+45>: leal   0x1(%rcx), %esi
bomb[0x400ffe] <+48>: callq  0x400fce                  ; <+0>
bomb[0x401003] <+53>: leal   0x1(%rax,%rax), %eax
bomb[0x401007] <+57>: addq   $0x8, %rsp
bomb[0x40100b] <+61>: retq   
{% endhighlight %}

仔细看会发现`<+20>`和`<+41>`是一样的，而他们的下一行判断正好相反。注意`<+24>`和`<+45>`,以及他们的下一行，都很类似。其实就是递归逼近答案。
好吧，随便带入一个0,结果发现正好就正确了。所以输入`0 0`。倒是测试了一下，发现输入`1 0`或者`3 0`或者`7 0`都正确，果然`func4`还要细看。只能带入func4慢慢推导，这里就不细写了。

##Phase5

{% highlight c-objdump %}
bomb`phase_5:
bomb[0x401062] <+0>:   pushq  %rbx
bomb[0x401063] <+1>:   subq   $0x20, %rsp
bomb[0x401067] <+5>:   movq   %rdi, %rbx
bomb[0x40106a] <+8>:   movq   %fs:0x28, %rax
bomb[0x401073] <+17>:  movq   %rax, 0x18(%rsp)
bomb[0x401078] <+22>:  xorl   %eax, %eax
bomb[0x40107a] <+24>:  callq  0x40131b                  ; string_length
bomb[0x40107f] <+29>:  cmpl   $0x6, %eax
bomb[0x401082] <+32>:  je     0x4010d2                  ; <+112>
bomb[0x401084] <+34>:  callq  0x40143a                  ; explode_bomb
bomb[0x401089] <+39>:  jmp    0x4010d2                  ; <+112>
bomb[0x40108b] <+41>:  movzbl (%rbx,%rax), %ecx
bomb[0x40108f] <+45>:  movb   %cl, (%rsp)
bomb[0x401092] <+48>:  movq   (%rsp), %rdx
bomb[0x401096] <+52>:  andl   $0xf, %edx
bomb[0x401099] <+55>:  movzbl 0x4024b0(%rdx), %edx
bomb[0x4010a0] <+62>:  movb   %dl, 0x10(%rsp,%rax)
bomb[0x4010a4] <+66>:  addq   $0x1, %rax
bomb[0x4010a8] <+70>:  cmpq   $0x6, %rax
bomb[0x4010ac] <+74>:  jne    0x40108b                  ; <+41>
bomb[0x4010ae] <+76>:  movb   $0x0, 0x16(%rsp)
bomb[0x4010b3] <+81>:  movl   $0x40245e, %esi
bomb[0x4010b8] <+86>:  leaq   0x10(%rsp), %rdi
bomb[0x4010bd] <+91>:  callq  0x401338                  ; strings_not_equal
bomb[0x4010c2] <+96>:  testl  %eax, %eax
bomb[0x4010c4] <+98>:  je     0x4010d9                  ; <+119>
bomb[0x4010c6] <+100>: callq  0x40143a                  ; explode_bomb
bomb[0x4010cb] <+105>: nopl   (%rax,%rax)
bomb[0x4010d0] <+110>: jmp    0x4010d9                  ; <+119>
bomb[0x4010d2] <+112>: movl   $0x0, %eax
bomb[0x4010d7] <+117>: jmp    0x40108b                  ; <+41>
bomb[0x4010d9] <+119>: movq   0x18(%rsp), %rax
bomb[0x4010de] <+124>: xorq   %fs:0x28, %rax
bomb[0x4010e7] <+133>: je     0x4010ee                  ; <+140>
bomb[0x4010e9] <+135>: callq  0x400b30                  ; symbol stub for: __stack_chk_fail
bomb[0x4010ee] <+140>: addq   $0x20, %rsp
bomb[0x4010f2] <+144>: popq   %rbx
bomb[0x4010f3] <+145>: retq
{% endhighlight %}

这道题挺让人头大的，只能参考一些资料。这里用到了一个逆向工具——radare2。

`r2 bomb`

进入radare2

首先执行`aaa`来初始化。

`afl`是用来标示函数的， 所以使用`afl~phase`来寻找反汇编中的phase，得到

{% highlight c-objdump %}
[0x00400c90]> afl~phase0x004015c4  149  8  sym.phase_defused0x00401062  146  9  sym.phase_50x00400f43  139  8  sym.phase_30x00400ee0  28  3  sym.phase_10x004012f6  37  1  sym.invalid_phase0x00401242  81  5  sym.secret_phase0x0040100c  86  7  sym.phase_40x004010f4  272  26  sym.phase_60x00400efc  71  8  sym.phase_2
{% endhighlight %}
使用`seek`来选择函数,`pdf`来打印反汇编的函数:

{% highlight c-objdump %}
[0x00400c90]> s sym.phase_5[0x00401062]> pdf/ (fcn) sym.phase_5 146|           ; CALL XREF from 0x00400eaa (sym.phase_5)|           0x00401062      53             push rbx|           0x00401063      4883ec20       sub rsp, 0x20|           0x00401067      4889fb         mov rbx, rdi|           0x0040106a      64488b042528.  mov rax, qword fs:[0x28]    ; [0x28:8]=0x48b8  ; '('|           0x00401073      4889442418     mov qword [rsp + 0x18], rax|           0x00401078      31c0           xor eax, eax|           0x0040107a      e89c020000     call sym.string_length|           0x0040107f      83f806         cmp eax, 6|       ,=< 0x00401082      744e           je 0x4010d2                |       |   0x00401084      e8b1030000     call sym.explode_bomb|      ,==< 0x00401089      eb47           jmp 0x4010d2               |      ||   ; JMP XREF from 0x004010d7 (sym.phase_5)|      ||   ; JMP XREF from 0x004010ac (sym.phase_5)|    ..---> 0x0040108b      0fb60c03       movzx ecx, byte [rbx + rax]|    ||||   0x0040108f      880c24         mov byte [rsp], cl|    ||||   0x00401092      488b1424       mov rdx, qword [rsp]|    ||||   0x00401096      83e20f         and edx, 0xf|    ||||   0x00401099      0fb692b02440.  movzx edx, byte [rdx + str.maduiersnfotvbylSo_you_think_you_can_stop_the_bomb_with_ctrl_c__do_you_] ; [0x4024b0:1]=109 LEA obj.array.3449 ; "maduiersnfotvbylSo you think you can stop the bomb with ctrl-c, do you?" @ 0x4024b0|    ||||   0x004010a0      88540410       mov byte [rsp + rax + 0x10], dl|    ||||   0x004010a4      4883c001       add rax, 1|    ||||   0x004010a8      4883f806       cmp rax, 6|    `====< 0x004010ac      75dd           jne 0x40108b               |     |||   0x004010ae      c644241600     mov byte [rsp + 0x16], 0|     |||   0x004010b3      be5e244000     mov esi, str.flyers         ; "flyers" @ 0x40245e|     |||   0x004010b8      488d7c2410     lea rdi, [rsp + 0x10]       ; 0x10 |     |||   0x004010bd      e876020000     call sym.strings_not_equal|     |||   0x004010c2      85c0           test eax, eax|    ,====< 0x004010c4      7413           je 0x4010d9                |    ||||   0x004010c6      e86f030000     call sym.explode_bomb|    ||||   0x004010cb      0f1f440000     nop dword [rax + rax]|   ,=====< 0x004010d0      eb07           jmp 0x4010d9               |   |||||   ; JMP XREF from 0x00401089 (sym.phase_5)|   |||||   ; JMP XREF from 0x00401082 (sym.phase_5)|   |||``-> 0x004010d2      b800000000     mov eax, 0|   ||`===< 0x004010d7      ebb2           jmp 0x40108b               |   ||      ; JMP XREF from 0x004010d0 (sym.phase_5)|   ||      ; JMP XREF from 0x004010c4 (sym.phase_5)|   ``----> 0x004010d9      488b442418     mov rax, qword [rsp + 0x18] ; [0x18:8]=0x400c90 section..text|           0x004010de      644833042528.  xor rax, qword fs:[0x28]|       ,=< 0x004010e7      7405           je 0x4010ee                |       |   0x004010e9      e842faffff     call sym.imp.__stack_chk_fail|       |   ; JMP XREF from 0x004010e7 (sym.phase_5)|       `-> 0x004010ee      4883c420       add rsp, 0x20|           0x004010f2      5b             pop rbx\           0x004010f3      c3             ret[0x00401062]> {% endhighlight %}
这题要求输入一个长度为6的字符串，经过一定的变换要得到`0x40245e`指向的字符串`flyers`。通过上述的代码，会敏感的发现待转换的字符串在`obj.array.3449`中，使用如下代码来找到偏移量
{% highlight c-objdump %}
[0x00401062]> px 16@obj.array.3449
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF0x004024b0  6d61 6475 6965 7273 6e66 6f74 7662 796c  maduiersnfotvbyl{% endhighlight %}
上面的一个偏移量对应下面的2个字符。

下面将flyers转化为十六进制ascii

{% highlight c-objdump %}
[0x00401062]> !rax2 -S flyers666c79657273
{% endhighlight %}

得到的`666c79657273`两个一组，找对应的上面的偏移量，可以得到偏移量list`[9, 0xF, 0xE, 5, 6, 7]`

使用python来计算出结果

{% highlight python %}
off = [9, 0xF, 0xE, 5, 6, 7]
result = ""
for c in off:
    result += chr(c + 64)

print result
{% endhighlight %}

所以这题的答案是`IONEFG`




