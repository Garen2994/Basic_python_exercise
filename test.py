# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date  : 2018-11-22 13:03:22
# @Author: Garen Hou
# GAREN'S PRACTICE DRAFT
# 10000 HRs
'''
#占位符
s1 = 72
s2 = 85
adv = (s2/s1 - 1) * 100
print('%s去年成绩是：%d,今年的成绩是：%d,提升了：%.1f%%'%('小明',s1,s2,adv))

#list操作
classmates = ['GarenHou','Moon','Hou','Sun']
classmates.append('Adam')
classmates.insert(4,'Skylar')
classmates.pop()
classmates.pop(2)
classmates[1] = 'MoonSun'
print(classmates[-2])
print(classmates)

#list性质
s = ['python','java',['asp','php'],'spring']
print(len(s))   #4个元素
print(s[2])
p = ['asp','php']
q = ['python','java',p,'go','node.js']
print(q[2])
print(q[2][1])  #q此时看作二维数组


#tuple元组
t = (1,2)
print(t)
e = ()
print(e)
a = (3,)
print(a)
b = (3)
print(b)

p = ('a','b',['A','B'])
p[2][0] = 'X'
p[2][1] = 'Y'
print(p)

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    ]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
'''
#条件判断

'''
age = 20
if age >= 18:
	print('your age is',age)
	print('adult')
else:
	print('child')

age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
'''

'''
x = 2
if x:
	print('True')
else:
	print('False')
'''

'''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

'''    

'''
import numpy as np
import random
a=np.random.randint(0,101,20)
def func(x):
    for i  in x:
        if i< 60:
            return i,'不及格'
        elif i>=60 and i<80:
            return i ,'及格'
        else:
            return i ,'优秀'
n=1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
'''
#使用continue打印出0-10之间的奇数
'''
n=0
while n < 10:
    n = n+1
    if n % 2 == 0:
       continue
    print(n)

print(type(range(5)))
print(type(list(range(8)))) 

'''
'''
#dict和set

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Adam'] = 97
d['Bob'] = 89
print(d['Adam'])
print(d)
print(d['Bob'])
print(d.get('Thomas'))
a = d.get('Thomas',-1)
print(d.pop('Bob'))
print(d)


key = (1,2,3)
d[key] = 'a list'
print(d)

s = set([1,2,3,4,5])
print(s)
a = set([1,2,3])
print(a) 
s.add(4)
a.add(10)
print(a)
print(s)

print(s & a)
print(s | a)

'''
'''
#不可变对象
a = ['b','a','t','e']
a.sort()
print(a)
'''
'''
a = 'abc'
b = a.replace('a','A') 
print(b)
print(a)
'''
#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
#test
'''
a=(1,2,3)
d0={'a0':a}    #将a作为key输入
print(d0['a0']) #不报错，证明不可变的tuple可作为dict的value

b=(1,2,3)
d3={a:'a1'}   #a也可以作为value
d3[a]
'a1'       不报错，则tuple也可作为dict的key

b=(1,[2,3])
d2={b:'b1'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'   #可变tuple不可作为dict的key 原因是list

b=(1,[2,3])
d2={'b2':b}
d2['b2']
(1, [2, 3])         #可变tuple可作为dict的value

a=(1,2,3)
s1=set(a)
s1        #不可变tuplea可被加入set
{1, 2, 3}

b=(1,[2,3])
s2=set(b))
a=(1,2,3)
d3={a:'a1'}   #a也可以作为value
d3[a]
      

b=(1,[2,3])
d2={b:'b1'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'   #可变tuple不可作为dict的key 原因是list

b=(1,[2,3])
d2={'b2':b}
d2['b2']
(1, [2, 3])         #可变tuple可作为dict的value

a=(1,2,3)
s1=set(a)
s1        #不可变tuplea可被加入set
{1, 2, 3}

b=(1,[2,3])
s2=set(b)
'''
'''
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x > 0:
        
        return x
    
    else:
        
        return -x

a = my_abs(-0.9)
print(a)
'''
'''
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
print(move(100,90,60,math.pi/6))
'''
#练习请定义一个函数quadratic(a, b, c)
'''
import math

def quadratic(a,b,c):

    if (math.pow(b,2) - (4*a*c)) < 0:
        print("此方程无解")

    else:
        x1 = ((-b) + math.sqrt(math.pow(b,2)-4*a*c)) / (2*a)
        x2 = ((-b) - math.sqrt(math.pow(b,2)-4*a*c)) / (2*a)
        return x1,x2
print(quadratic(1,-4,0))
'''
'''
def power(x,n=2):
    
    s = 1
    while n > 0:
        n = n - 1
        s = s * x 
    return s
a = power(5,3)
b = power(3)
print(a)
print(b)


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Garen','女',city='西安'))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end()) #有多个END，函数似乎记住了上次加了END的list，因此默认参数必须指向不变对象
'''
'''
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
'''
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum  + n*n
    return sum
print(calc(1,2,3))
'''
'''
def calc(*numbers):   #星号*表示可变参数list和tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2],4,5)) #参数个数随时加减
print(calc(*nums,4,5)) #在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
'''
'''
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print(person('Garen',25,city='Beijing',job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('Jack', 24, **extra,code=130052)) #仍然可以传入不受限制的关键字参数
'''
'''
def person(name,age,*,city,job):
    print(name,age,city,job)
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('Garen',25,city='Beijing',job='Engineer'))
#print(person('Jack', 24, **extra,code=130052)) #报错code
print(person('Garen',25,'Beijing','Engineer'))
'''
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#nums = [1,2,3]
#extra = {'city': 'Beijing', 'job': 'Engineer'}
#print(f1(1,2,3))
#print(f1(1,2,3,*nums,**extra))

nums = (1,2,3,4,5)
extra = {'d': 99, 'x': '#'}
print(f1(*nums,**extra)) #对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
'''
#递归
'''
def fact(n):
    if n == 1:
        return 1
    return fact(n-1)*n
print(fact(5))
'''
#尾递归
'''
def fact(n):
    
    return fact_iter(n,1)

def fact_iter(num,product):
  
    if num == 1 :
        return product
    return fact_iter(num-1,num*product)

print(fact(100))
'''
#用递归函数实现汉诺塔的移动
'''
def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(2,'A','B','C')
'''
#切片slice
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
i,j = 2,4
print(L[i:j])

s = '0123456789'
print(int(s[1:4])+1)

t = ('1','2','3','4')
print(t[1:3])
'''
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
'''
def trim(s):
    if s !='':
        while s[:1] == ' ':
            s = s[1:]
        while s[-1:] == ' ':
            s = s[:-1]
    return s
print(trim('  hello '))
'''
'''
from collections import Iterable
print(isinstance('ABC',Iterable))#str是否可迭代 True
print(isinstance(123,Iterable))#z整数是否可迭代 False
d = {'a' : 1,'b' : 2,'c' : 3}
print(isinstance(d,Iterable))#字典可迭代
'''
'''
for i, value in enumerate(['A', 'B', 'C']):#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
    print(i, value)


for i,j in [(1,10),(2,11),(3,12)]:
    print(i,j)
'''
#使用迭代查找一个list中最小和最大值，并返回一个tuple
'''
def find_max_and_min(L):
    if len(L) == 0:
        return(None,None)
    min=max=L[0]
    for i in L:
        if i < min:
            min = i
        elif i > max:
            max = i
    return (min,max)

print(find_max_and_min([1,2,7,8,9,3,5]))
'''
#列表生成式
'''
L = [x*x for x in range(1,11)]
print(L)
#带if判断
c = [-1,3,-3,4,-5,-6,7,5]
b = [x for x in c if x > 0]
print(b)
#多个列表运算
a = [1,2,3,4,5]
d = ['a',"b","c","d","e"]
e = [str(x)+str(y)+str(z) for x , y , z in zip(a,d,c)]
print(*zip(a,d,c))
print(e)

l = [m+n for m in 'XYZ' for n in 'ABC']
print(l)
'''

#生成器、迭代器
'''
L = [x*x for x in range(1,11)]
print(L)

G = (x*x for x in range(1,11))

for i in G:
    print(i)
'''
'''
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'node'
f = fib(6)
print(f)
for i in f:
    print(i)
'''

#生成器函数打印杨辉三角
'''
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]#首尾不变，生成中间部分

#测试部分
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
'''
'''
#生成一个1000万个数字的列表，分别使用列表生成式和生成器时返回结果的时间和所占内存空间的大小
import time
import sys

time_start = time.time()
g1 = [x for x in range(10000000)]
time_end = time.time()
print('列表生成式返回结果花费的时间： %s' % (time_end - time_start))
print('列表生成式返回结果占用内存大小：%s' % sys.getsizeof(g1))

def my_range(start, end):
    for x in range(start, end):
        yield x

time_start = time.time()
g2 = my_range(0, 10000000)
time_end = time.time()
print('生成器返回结果花费的时间： %s' % (time_end - time_start))
print('生成器返回结果占用内存大小：%s' % sys.getsizeof(g2))
'''

#高阶函数：函数式编程
#****函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数***

'''
a = abs(-10)
print(a)

f = abs
b = f(-10)
print(b)
'''
'''
def add(x,y,f):

    return f(x) + f(y)

print(add(-10,-9,abs)) #abs函数名作为参数传入 add就是一个高阶函数啦
'''
'''
#map函数

def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

print(list(map(abs, [-1, -2, -3, -4, 5, -6, -7, 8, 9]))) 
'''
#reduce函数
'''
from functools import reduce

def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))


def char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]

def fn(x,y):
    return x * 10 + y 
print(reduce(fn,map(char2num,'13579')))
print(isinstance(reduce(fn,map(char2num,'13579')),int))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):#相当于int()的功能
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('1345'))  
'''

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

'''from functools import reduce

L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name.capitalize()
    
L2 = list(map(normalize, L1))
print(L2)

#sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x,y : x*y, L)
print(prod([1,2,3,4,5]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    s1,s2 = s.split('.')
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x,y : x*10+y , map(char2num,s1)) + reduce(lambda x,y : x*10+y , map(char2num,s2))/pow(10,len(s2))
print(isinstance(str2float('123.456'),float))
print(str2float('123.456'))
'''
# filter函数
'''from functools import reduce
def is_odd(n):
    return n % 2 == 1
print(reduce(lambda x,y:x*10+y,list(filter(is_odd,[1,2,3,4,5,6,7,9]))))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

'''
#埃氏筛法计算素数
'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
#用filter()计算出回数12321,909等
'''
'''
def is_palinderome(n): 
    return str(n) == str(n)[::-1] #s[::1]实现字符串翻转           
print(list(filter(is_palinderome,range(1,1000))))
'''
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return (t[1])

L1 = sorted(L, key=by_name)
print(L1)

L2 = sorted(L , key=by_score , reverse = True)
print(L2)
'''

#返回函数
'''
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3,4,5,6))   

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum #返回求和的函数
f1 = lazy_sum(1,2,3,4,5,6)
f2 = lazy_sum(1,2,3,4,5,6)

print(f1) 
print(f1())
print(f1==f2)
print(f1()==f2()) #每次调用都会返回一个新的函数，即使传入相同的参数.f1()和f2()的调用结果互不影响
'''
'''
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())

'''
'''
def count():
    def f(j):
        def g():
            return  j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())
'''
#利用闭包返回一个计数器函数，每次调用它返回递增整数
'''
def createCounter():
    a = 0
    def counter():
        nonlocal a
        a += 1 #要么a说明使用外层变量；要么a就要是个容器(如下)
        return a
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
#a = [0]只会在counterA = createCounter()赋值语句时执行，调用counterA()只执行counter()函数，并且可以使用a这个变量。

def createCounter():
    a = [0]
    def counter():
        a[0] = a[0]+1 
        return a[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
'''
'''
def now():
    print('2015-3-25')
f = now
print(now.__name__)
print(f.__name__)
'''
'''
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')
now()
print(dir(log))
'''
'''
def a_new_decorator(a_func):
 
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
 
        a_func()
 
        print("I am doing some boring work after executing a_func()")
 
    return wrapTheFunction
@a_new_decorator
#the @a_new_decorator is just a short way of saying:
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"
'''
#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start = time.time() #计算函数执行时间
        result = fn(*args,**kw)
        stop = time.time()
        print('%s executed in %s ms' % (fn.__name__, (stop-start)*1000))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)

print(f)
print(fast.__name__) 
s = slow(11, 22, 33)
print(s)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')