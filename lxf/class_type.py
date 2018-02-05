#!/usr/bin/python
# coding:utf-8

from hello import Hello

h = Hello()
h.hello()
# Hello, world.
print(type(Hello))
# <type 'type'>
print(type(h))
# <class 'hello.Hello'>


# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self, name='world'):     # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))     # 创建Hello class