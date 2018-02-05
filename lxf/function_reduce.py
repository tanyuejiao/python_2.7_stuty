#!/usr/bin/python
# coding:utf-8
# reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
from functools import reduce


def add(x, y):
    return x + y
a = reduce(add, [1, 3, 5, 7, 9])
print a


# 如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def con(x, y):
    return str(x)+str(y)
a = reduce(con, [1, 3, 5, 7, 9])
print a


def con1(x, y):
    return x*10 + y
a = reduce(con1, [1, 3, 5, 7, 9])
print a