#!/usr/bin/python
# coding:utf-8

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
# 可以使用isinstance()判断一个对象是否是Iterable对象：
# str是否可迭代
a = isinstance("abc", Iterable)
print ("a: %s" % a)
# list是否可迭代
a = isinstance([1, 2, 3], Iterable)
print ("a: %s" % a)
# 整数是否可迭代
a = isinstance(123, Iterable)
print ("a: %s" % a)
a = isinstance((x for x in range(10)), Iterable)
print ("a: %s" % a)
# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 0 A
# 1 B
# 2 C
# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)