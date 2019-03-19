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

'''age = 20
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

'''x = 2
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
'''n=0
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
print(fact(1000))
'''
#March.19th 终于会把代码同步到Github了哈哈哈