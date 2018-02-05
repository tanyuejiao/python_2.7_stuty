#!/usr/bin/python
# coding:utf-8


# 我们在函数lazy_sum中又定义了函数sum1，并且，内部函数sum1可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum1时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum1
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
print lazy_sum(1, 2, 3, 4)
f = lazy_sum(1, 2, 3, 4)
print f
# 调用函数f时，才真正计算求和的结果：
# <function sum at 0x02657770>
# lazy_sum(1,2,3,4,5)返回的是一个指向求和的函数的函数名。
# 在调用lazy_sum(1,2,3,4,5)的时候，不立刻求和，而是根据后面代码的需要在计算。
print f()

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1
print f2
print f1 == f2
# False
# lazy_sum()每调用一次，都会返回一个独一无二的函数地址。

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
