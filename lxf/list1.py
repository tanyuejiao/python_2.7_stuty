#!/usr/bin/python
# coding:utf-8

# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)  # 4
# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])