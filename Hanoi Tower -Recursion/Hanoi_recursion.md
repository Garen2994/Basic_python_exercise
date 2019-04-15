### 用递归解决汉诺塔移动问题

- #### python代码

```python

```

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

![](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1555322362006.png)

![](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1555322507864.png)

流程图理解3个圆块情况的递归函数调用：

![](C:\Users\Administrator\Desktop\v2-59507a712f50971601587cc970f75904_r.jpg)