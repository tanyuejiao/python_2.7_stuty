#!/usr/bin/python
# coding:utf-8
# from collections import Iterator,Iterable


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print r
print list(r)

# map()作为高阶函数，事实上它把运算规则抽象了，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
r = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print r