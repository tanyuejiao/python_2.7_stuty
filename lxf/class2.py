#!/usr/bin/python
# coding:utf-8
import types
'''获取对象信息
当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
使用type()
首先，我们来判断对象类型，使用type()函数：
基本类型都可以用type()判断：'''

print type(123)
# <class 'int'>
print type('str')
# <class 'str'>
print type(None)
# <type(None) 'NoneType'>


# 如果一个变量指向函数或者类，也可以用type()判断：
def abs():
    pass


class Animal(object):
    def __init__(self):
        print "animal"
a = Animal()
print type(abs)
# <class 'builtin_function_or_method'>

print type(a)
# <class '__main__.Animal'>

# 比较两个变量的type类型是否相同：
print type(123) == type(456)
# True
print type(123) == int
# True
print type('abc') == type('123')
# True
print type('abc') == str
# True
print type('abc') == type(123)
# False


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
def fn():
    pass
print type(fn) == types.FunctionType
# True
print type(abs) == types.BuiltinFunctionType
# True
print type(lambda x: x) == types.LambdaType
# True
print type((x for x in range(10))) == types.GeneratorType
# True
# 能用type()判断的基本类型也可以用isinstance()判断：
print isinstance('a', str)
# True
print isinstance(123, int)
# True
print isinstance(b'a', bytes)
# True

# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print isinstance([1, 2, 3], (list, tuple))
# True
print isinstance((1, 2, 3), (list, tuple))
# True

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print dir('ABC')