#!/usr/bin/python
# coding:utf-8
import os   # 导入os模块，模块的概念后面讲到
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
a = list(range(1, 11))
print a

L = []
for x in range(1, 11):
    L.append(x * x)
print L

# 列表生成式则可以用一行语句代替循环生成上面的list
a = [x*x for x in range(1, 11)]
print a

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
a = [x * x for x in range(1, 11) if x % 2 == 0]
print a
# [4, 16, 36, 64, 100]

# 使用两层循环，可以生成全排列：
a = [m + n for m in 'ABC' for n in 'XYZ']
print a
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
a = [d for d in os.listdir('.')]
print a

# 列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
a = [k + '=' + v for k, v in d.items()]
print a

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
# print [s.lower() for s in L]

# 使用内建的isinstance函数可以判断一个变量是不是字符串：
s = []
for x in L:
    if isinstance(x, str):
        s.append(x.lower())
    else:
        s.append(x)
print s

