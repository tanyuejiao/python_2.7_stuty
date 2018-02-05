#!/usr/bin/python
# coding:utf-8

a = sorted([36, 5, -12, 9, -21])
print a
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print sorted([36, 5, -12, 9, -21], key=abs)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)