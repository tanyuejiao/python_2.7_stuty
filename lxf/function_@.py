#!/usr/bin/python
# coding:utf-8


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2015-3-25')
f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print now.__name__
print f.__name__


