#!/usr/bin/python
# coding:utf-8
# ict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print value
for key, value in d.items():
    print (key + "=>" + str(value))
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABC':
    print(ch)