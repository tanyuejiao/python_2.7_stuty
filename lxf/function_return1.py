#!/usr/bin/python
# coding:utf-8


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
    fs.append(f)
    return fs

f1 = count()
f2 = count()
f3 = count()
print f1
print f2
print f3
print f1()
print f2()
print f3()