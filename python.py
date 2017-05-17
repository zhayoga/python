#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 'end'
ln = [1,2,3,4,5,6,7,8,9]
ls = ['a','b','c','d','e','f']
tn = (1,2,3,4,5,6,7,8,9)
ts = ('a','b','c','d','e','f')


#第一个Python程序-2017.3.31
'''
name=input("Who are you:") 
print("hello",name,"isit",2012+5,"year.")    
'''

#Python基础-2017.3.31
    #1.数据类型和变量
'''
print("I\'m OK!\\\n\t?")#\n表示换行 \t表示制表符
print(r'\\')#r'\\'内部的字符串默认不转义

True and False#False 交集
True or False#True 并集
not True#False 

if 3>2:
    print('>')
else:
    print('<')
#print(PI)#PI = 3.14159265359 需要数学库

print(10/3)#浮点除
print(10//3)#地板除
print(10%3)#取余

#inf(无限大)
'''
    #2.字符串和编码
'''
print(ord('张'),ord('永'),ord('刚'))#Python提供了ord()函数获取字符的整数表示
print(chr(ord('张')))#chr()函数把编码转换为对应的字符

print(b'abc')#对bytes类型的数据用带b前缀的单引号或双引号表示
print('abc'.encode('ascii'))#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('abc'.encode('utf-8'))#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('张永刚'.encode('utf-8'))#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('张永刚'.encode('gb2312'))#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print(b'decode'.decode('ascii'))#从网络或磁盘上读取了字节流，读到的数据是bytes。
#要把bytes变为str，就需要用decode()方法

print(len('abc'))#len()函数计算的是str的字符数
print(len('张永刚'))#计算str包含多少个字符
print(len('张永刚'.encode('utf-8')))#计算bytes的字节数

print('abc'.replace('a','z'))#.replace()替换

print('is %s or %f !'%('SB',14.5))#格式化 %%
#%d 整数,%f 浮点数,%s 字符串,%x 十六进制整数

a='a'
n=1
for n in range(50):#打印ASCII编码
    print(a)
    n=n+1
    a=chr(ord(a)+1)
'''

    #3.使用list和tuple
'''
print(['a','b','c'])#列表:list是一种有序的集合
l=['a','b','c']
print(len(l))#len()函数可以获得list元素的个数
print(l[0])
print(l[1])
print(l[2])
print(l[-1])
print(l[-2])
l.append('end')#append()追加元素到末尾
print(l[-1])
l.insert(0,'here')#insert()元素插入到指定的位置
print (l[0])
l.pop()#pop()删除list末尾的元素
print(l[-1])
l.pop(0)#pop()删除指定位置的元素
print(l[0])
l[0]=1#赋值
print(l[0])

l.sort()#对list排序

l=[[1,2,3],[4,5,6],[7,8,9]]#list二维数组
print(l[2][1])#list[X][Y]
print(l)

t=(1,2,'三')#元组：tuple,是不可变的有序的集合
print(t)
t=(1,)#一个元素的tuple
'''
    #4.条件判断
'''
if True:
    print('Yes')#如果真则执行
elif True:
    print('agin')#如果真则执行
else:
    print('No')#如果假则执行

age=input('age:')
if int(age)>18:#input()返回的数据类型是str
    print('Yes')
else:
    print('No')

#根据BMI公式（体重除以身高的平方）计算他的BMI指数范围
height=int(input("你的身高是?(单位为厘米):"))/100
weight=int(input("你的体重是?(单位为公斤):"))
BMI=weight/(height*height)
ans='结果'
if BMI<=18.5:
    ans='过轻'
elif BMI<=25:
    ans='正常'
elif BMI<=28:
    ans='过重'
elif BMI<=32:
    ans='肥胖'
else:
    ans='严重肥胖'
print('计算结果是你的体重为%s,你的BMI指数是%.1f.'%(ans,BMI))
'''
    #5.循环
'''
sum=0
for a in range(101):#if循环
    sum=sum+a
print(sum)
sum=0
b=1
while b<100:#while循环
    sum=sum+b
    b=b+2
    if b>50:
        break#break语句会结束当前循环,不要滥用
        continue#continue语句会直接继续下一轮循环，后续的语句不会执行,不要滥用
print(sum)
'''
    #6.使用dict和set
'''
d={'a':1,'b':2,'c':3,'d':4}#dict字典全称dictionary，在其他语言中也称为map，
#使用键-值（key-value）存储，具有极快的查找速度。
#dict的key必须是不可变对象,哈希算法
d['b']=11
if 'c' in d:#in dict 返回kay是否在dict内
    print(d['c'])
print(d.get('c'))#.get() 返回kay的值
print(d.pop('a'))#.pop(kay) 删除kay-value
print(d)

s=set([1,2,2,3,4,4,5])#set和dict类似，也是一组key的集合，但不存储value
#在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合
print(s)
s.add(6)#.add()添加元素到set中
print(s)
s.remove(6)#.remove()可以删除元素
print(s)
s1=set([1,2,3])
s2=set([3,4,5])
print(s1&s2)#求交集
print(s1|s2)#求并集
#key必须是不可变对象,不可变对象,不可变对象:str,int
#list是可变对象
'''
    #7.函数
#默认参数、可变参数、关键字参数和命名关键字参数
'''
print(abs(-123))#求绝对值
print(max(1,2,3,4,7))#求最大值
print(int('2134124'))#转换为int整数
print(float('3.14'))#转换为浮点数
print(str(3.14))#转换为字符
print(bool(0))#转换为布尔值
a=abs#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量
print(a(-213))
print(hex(213))#转换为十六进制
#英文很重要！

def zyg(z):#定义函数
    if not isinstance(z, (int, float)):#数据类型检查
        raise TypeError('bad operand type')#自动检查出来，并抛出TypeError,还有ValueError
    if z > 0:
        return z,-z
    else:
        return -z,z
print(zyg(-666))
#from zyg improt zyg#导入模块
def zzz():
    pass#pass可以用来作为占位符

def power(x,n=2):#函数传入的参数,默认参数值,默认参数必须指向不变对象！
    a = 1
    while n > 0:
        a = a * x
        n = n - 1
    return a
print(power(2,32))

def add_end(L=[]):#每次调用该函数，如果改变了L的内容，则下次调用时，
#默认参数的内容就变了，不再是函数定义时的[]了。
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
#我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

def zyg(*args):#可变参数tuple
    for a in args:
        print(a)
    return
a=[1,2,3]
zyg(*a)#传入tuple

def zyg(x,**kw):#关键字参数dict
    print(x)
    print(kw)
    return
zyg('a',a='1')#a='a'关键字
a={'a':'1','b':'2','c':'2',}
zyg('a',**a)#dict的所有key-value用关键字参数传入到函数的**num参数

def zyg(x,*,kw1,kw2):#位置参数+命名关键字参数dict
    print(x)
    print(kw1)
    print(kw2)
    return
zyg('a',kw1='1',kw2='2')

def zyg(x,*args,kw1,kw2):#位置参数+可变参数tuple+命名关键字参数dict
    print(x)
    print(y)
    print(kw1)
    print(kw2)
    return
zyg('a',1,2,kw1='1',kw2='2')
'''
    #8.递归函数
'''
def move(n,a,b,c):#汉诺塔的移动3个柱子A、B、C把所有n个盘子从A借助B移动到C的方法
    if n == 1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(10,"A","B","C")
'''

#高级特性 
'''
#代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

    #1.切片
l=[1,2,3,4]
print(l[1:3])#切片（Slice）操作符
print(l[:3])
print(l[-2:])
print(l[::2])#每隔两个数取一个
t=(1,2,3,4,)
print(t[2:4])#tuple也可以用slice切片
s='abcde'
print(s[2:4])
d={'a':1,'b':2,'c':3,'d':4}

    #2.迭代
for i in l:#遍历我们称为迭代（Iteration）
    print(i)
for key in d:#迭代字典
    print(key)
for value in d.values():#迭代字典
    print(value)
for s in 'abcd':#迭代字符串
    print(s)

from collections import Iterable
print(isinstance('abc',Iterable))#判断是否可迭代T
print(isinstance(123124,Iterable))#F

for i,j in enumerate(['a','b','c']):#对list实现类似Java那样的下标循环,
#enumerate函数可以把一个list变成索引-元素对
    print(i,j)
for x,y in [(2,3),(4,5)]:#for 同时引用了两个变量
    print(x,y)

    #3.列表生成式
print(list(range(2,6)))#列表生成式即List Comprehensions
print(tuple(range(2,6)))
print([x+x for x in range(1,5)])
print([x+x for x in range(1,5) if x % 2 == 0])#or循环后面还可以加上if判断
print([x+y for x in 'abc' for y in 'xyz'])#使用两层循环

d={'a':'1','b':'2','c':'3','d':'4'}
print([x + '=' + y for x,y in d.items()])#.items()列出dict的所有key-value

l=['SADAWD','ASFDQWFQW','dfqwefweaf']
print([x.lower() for x in l])#把一个list中所有的字符串变成小写

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]#把一个list中所有的字符串变成小写
print(L2)

    #4.生成器generator(把return替换为yield)

g = (x for x in range(1,5))
for n in g:#使用for循环因为generator也是可迭代对象
    print(n)

def fib(max):#斐波拉契数列（Fibonacci）用函数实现
    n,a,b = 0,1,1
    print(a)
    while n < max:
        print(b)
        a,b = b,a+b#t = (b, a + b); a = t[0]; b = t[1]
        n = n + 1
    print('done')
    return
fib(10)

def fib(max):#斐波拉契数列（Fibonacci）用生成器实现
    n,a,b = 0,1,1
    yield a
    while n < max:
        yield b
        a,b = b,a+b#t = (b, a + b); a = t[0]; b = t[1]
        n = n + 1
    return "miss"
for x in fib(10):
    print(x)
#最难理解的就是generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。

g = fib(10)
while True:#拿不到generator的return语句的返回值,如果想要拿到返回值，
#必须捕获StopIteration错误，返回值包含在StopIteration的value中
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


#杨辉三角定义

def triangles():#第一版
    l1 = [1,]
    l2 = [1,]
    n = 1
    yield l1
    while True:
        l1 = l1 + [0,] 
        l2 = l2 + [0,] 
        n = n + 1
        x = 0
        y = 0
        while x < len(l1):
            l1[x] = l2[x-1]+l2[x]
            x = x + 1
        for n in range(0,len(l1)):
            l2[n] = l1[n]
        yield l1  
    return 'done'

def triangles():#第二版
    l1 = [1]
    while True:
        yield l1
        l2 = l1+[0]
        n = len(l2)
        l1 = [l2[n-x] + l2[n-x-1] for x in range(1,n+1)]
    return 'done'

t = triangles()
n = 0
for x in t:
    print(x)
    n = n + 1
    if n == 10:
        break


    #5.迭代器

#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
from collections import Iterable
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections import Iterator
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
isinstance({}, Iterator)
isinstance('abc', Iterator)
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)
#所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
'''

#函数式编程-2017.4.3
#高阶函数,那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
'''
x = abs#函数本身也可以赋值给变量，即：变量可以指向函数。
print(x(-124))

def add(x,y,f):#函数式编程就是指这种高度抽象的编程范式
    return f(x) + f(y)
print(add(2,-3,abs))

    #1.map/reduce

#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x*x
print(list(map(f,[1,2,3])))#map把结果作为新的Iterator返回,
#通过list()函数让它把整个序列都计算出来并返回一个list

print(list(map(str,[1,2,3,4,5])))

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x,y):
    return x*10 + y
x = reduce(fn,[1,2,3,4,5])


def str2int(s):
    return reduce(lambda x, y: x * 10 + y,map(lambda z: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[z],s))
x = str2int('12341234')

def normalize(name):#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
    return name.lower().capitalize()
x = list(map(normalize,['sadfQ','Qfewf']))

from functools import reduce
def prod(l):#接受一个list并利用reduce()求积
    return reduce(lambda x, y: x * y,l)
x = prod([2,3,4])

from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2float(s):#把字符串'123.456'转换成浮点数123.456：
    a,b = s.split('.')
    b = b[::-1]
    c = reduce(lambda x, y: x*10 + y,map(char2num,a))
    d = reduce(lambda x, y: x*0.1 + y,map(char2num,b))
    f = d * 0.1
    return c + f  
x = str2float('123.456')        
'''
    #2.filter
'''
#filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素,
#返回的是一个Iterator,用list()函数获得所有结果并返回list

def is_odd(n):
	return n % 2 == 1
x = list(filter(is_odd,tn))

def not_empty(s):
	return s.strip() and s
x = list(filter(not_empty,ts + (' ','	')))

#计算素数的一个方法是埃氏筛法
def odd3():#构造一个从3开始的奇数序列
	n = 1
	while True:
		n = n + 2
		yield n

def not_di(n):
	return lambda x : x % n != 0 #x不是n的倍数返回True

def prime():
	x = odd3()
	n = 1
	while True:
		n = next(x)
		yield n
		x = filter(not_di(n), x)

p = prime()
for n in range(100):#求从3之后第100个素数
	next(p)
x = next(p)

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def nn():#构造一个从1开始的数列
	n = 0
	while True:
		n = n + 1
		yield n
def is_mi(n):#第一版
	s = str(n)
	l = len(s)
	for m in range(l):
		if s[m:m+1] != s[l-m-1:l-m]:
			return False
	return True
def is_mi2(n):#第二版
	s = str(n)
	s2 = s[::-1]
	if s2 == s:
		return True
	return False
def pal(n):
	m = nn()
	x = filter(is_mi2, m)
	for y in range(n):
		next(x)
	return next(x)
		
x = pal(1000)#求第1000个回数
'''
	#4.sortld
#用sorted()排序的关键在于实现一个映射函数
'''
sorted([36, 5, -12, 9, -21], key=abs)
[-21, -12, 5, 9, 36]

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):#按名字排序
	return t[0]
def by_score(t):#按成绩排序
	return t[1]
L2 = sorted(L, key = by_name)
print('按名字排序:',L2)
L3 = sorted(L, key = by_score, reverse = True)
print('按成绩排序:',L3)
'''
	#5.返回函数
'''
def la_sum(*args):#可变参数tuple
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
#这种称为“闭包（Closure）”的程序结构拥有极大的威力。
	def sum():
		n = 0
		for m in args:
			n = n + m
		return n
	return sum

la = la_sum(*tn)#传入tuple
x = la()

def co():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1,f2,f3 = co()
print(f1())
print(f2())
print(f3())
#返回函数不要引用任何循环变量，或者后续会发生变化的变量

def co():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 = co()
print(f1())
print(f2())
print(f3())
#再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变
'''
	#6.匿名函数
'''
x = list(map(lambda x: x*x, ln))

def build(x, y):#也可以把匿名函数作为返回值返回
    return lambda: x * x + y * y
f = build(2,3)
x = f()#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
x = f.__name__#函数对象有一个__name__属性，可以拿到函数的名字<lambda>
'''
    #7.装饰器decorator
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log#@语法，把decorator置于函数的定义处 #now = log(now)
def new():
    print('2017-4-11')
f = new
f()#通过变量也能调用该函数

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)#wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('me')#@语法，把decorator置于函数的定义处 #now = log('execute')(now)
def new():
    print('2017-4-11')
new()
x = new.__name__

import functools
def log(func):
    @functools.wraps(func)#wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        x = func(*args, **kw)
        print('end call %s():' %  func.__name__)
        return x
    return wrapper
@log#@语法，把decorator置于函数的定义处 #now = log(now)
def new():
    print('2017-4-11')
new()
x = new.__name__

import functools
def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)#wrapper.__name__ = func.__name__
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        def wrapper(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)
        return wrapper
@log#('me')
def new():
    print('2017-4-11')
new()
x = new.__name__
'''
    #8.偏函数Partial function
''' 
x = int('123', base=16)
#x = int('123', 16)   

def int16(i):
    return int(i, 16)
x = int16('123')

import functools
int2 = functools.partial(int, base=2)#固定**kw #functools.partial的作用就是，
#把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。
x = int2('11010101010')

max2 = functools.partial(max, 10)#添加到*args中
x = max2(1,2,3,4)
'''
    #9.模块module,包package
#C:\Users\zyg\Desktop\python\mypackage\holle.py
#外部不需要引用的函数全部定义成私有private，只有外部需要引用的函数才定义为公开public。
#第三方模块处理图像的工具库Pillow
'''
from PIL import Image
im = Image.open('test.png')
x = (im.format, im.size, im.mode)
im.thumbnail((200,300))
im.save('thumb.jpg','JPEG')
#找个图片生成缩略图
'''
#面向对象编程-2017.4.11
    #1.类（Class）和实例（Instance）,数据封装、继承和多态是面向对象的三大特点
'''
class student(object):
    def __init__(self, name, score):
        self.__name = name#实例的变量名如果以__开头，就变成了一个私有变量（private）
        #只有内部可以访问，外部不能访问
        self.__score = score
    def print_score(self):#对象的方法（Method）
        print('%s:%s' % (self.name,self.score))
    def get_score(self, score):
        self.score = score
    def get_grade(self):
        if self.score < 60:
            return 'C'
        elif self.score > 90:
            return 'A'
        else:
            return 'B'
s = student('AA', 99)
s.get_score(59)
x = s.get_grade()
s.print_score()
'''
    #2.访问限制

#实例的变量名如果以__开头，就变成了一个私有变量（private）
#只有内部可以访问，外部不能访问

#变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的
#是特殊变量，特殊变量是可以直接访问的，不是private变量

    #3.继承和多态
'''
class Animal(object):
    def __len__(self):
        return 100
    def run(self):
        print('Animal is runing!')
an = Animal()
an.run()
x = len(an)

class Dog(Animal):
    def run(self):
        print('Dog is runing!')
class Cat(Animal):
    def run(self):
        print('Cat is runing!')
do = Dog()
ca = Cat()
do.run()
ca.run()
#判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(an, Animal), isinstance(do, Dog), isinstance(ca, Cat))
print(isinstance(do, Animal), isinstance(an, Dog))
print(isinstance(an, (Animal, Dog)))
#要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
def run2(animal):
    animal.run()
    animal.run()

run2(an)
run2(do)
run2(ca)
#“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
#一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
class Time(object):
    def run(self):
        print('TK.TK.TK...')

ti = Time()
run2(ti)
#许多对象，只要有read()方法，都被视为“file-like object“。
'''
    #4.获取对象信息
'''
x = type('x')
x = type(12) == int

import type

>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True

def len2(x):
    return x.__len__()
x = len2('asd')

class My(object):
    def __init__(self):
        self.x = 2
    def power(self):
        self.x = self.x * self.x
m = My()
print(hasattr(m, 'x'))
print(hasattr(m, 'y'))
print(setattr(m, 'y', 5))
print(hasattr(m, 'y'))
print(getattr(m, 'y'))
print(m.y)
print(getattr(m, 'z', 404))
f = getattr(m, 'power')
f()
print(m.x)

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
'''
    #5.实例属性和类属性
    
    
#面向对象高级编程
    #1.使用__slots__
'''
class Dog(object):
    __slots__ = ('age', 'name','set_age','len')
d = Dog()
d.name = 'wang'
print(d.name)
def set_age(self, age):
    self.age = age
from types import MethodType
d.set_age = MethodType(set_age, d)#给实例绑定一个方法
d.set_age(12)
print(d.age)
d2 = Dog()
Dog.set_age = set_age#为了给所有实例都绑定方法，可以给class绑定方法
d2.set_age(13)
print(d2.age)

#定义一个特殊的__slots__变量，来限制该class实例能添加的属性
#__slots__ = ('age', 'name','set_age','len')
d.len = 100

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#在子类中也定义__slots__，这样，
#子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
    #2.使用@property,装饰器就是负责把一个方法变成属性调用的
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score is not integer!')
        if value < 0 or value > 100:
            raise ValueError('score is not in 0~100!')
        self._score = value

s = Student()
s.score = 66
x = s.score
'''
    #3.多重继承MixIn
'''
class Boy(object):
    pass
class Girl(object):
    pass

class Student(object, Boy):
    pass
#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#只允许单一继承的语言（如Java）不能使用MixIn的设计
'''

    #4.定制类
'''
#__str__(self):作用于print()的显示内容
#__reper__(self):__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串

#__iter__(self):返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
#拿到循环的下一个值，直到遇到StopIteration错误时退出循环

#__getitem__(self, value):>>> f = Fib(),#>>> f[0]
#__setitem__()
#__delitem__()

#__call__()>>> s = Student('Michael'),>>> s() # self参数不要传入
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
#所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
#因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
#能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
#>>> callable(Student())
#True

#__getatter__()
class Student(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, attr):
        if attr == 'score':
            return 66#返回函数也是完全可以的

s = Student('zz')
print(s.name)
print(s.score)
'''
    #5. 枚举类

from enum improt Enum
Month = Enum('Month',(''Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec''))




















print(x)


#期末总结,see me!!!
input("new you can see!") 











































