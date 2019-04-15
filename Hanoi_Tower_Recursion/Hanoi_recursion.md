### 用递归解决汉诺塔移动问题

- #### python代码

```
def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3,'A','B','C')
```

- #### 理解

 无论多少个圆块，可以抽象成为同一套思路：就是想办法把(n-1)个a柱上的圆块先移动到b柱，然后把最底部最大的一个圆块移动到c柱，最后把b柱上的(n-1)个圆块移动到c柱。

可用断点调试查看2个圆块情况的递归，如下：

![](https://github.com/Garen2994/Image/blob/master/img/001.png)

![](https://github.com/Garen2994/Image/blob/master/img/002.png)

流程图理解3个圆块情况的递归函数调用：

![](https://github.com/Garen2994/Image/blob/master/img/hanoi.jpg)