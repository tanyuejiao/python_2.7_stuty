#!/usr/bin/python
# coding:utf-8
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print g
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print g.next()
print g.next()
print next(g)
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
for i in g:
    print i