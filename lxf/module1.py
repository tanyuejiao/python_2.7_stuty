#!/usr/bin/python
# coding:utf-8
# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '

__author__ = 'Michael Liao'

import sys


def test():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
    # 运行python3 hello.py获得的sys.argv就是['hello.py']；
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
