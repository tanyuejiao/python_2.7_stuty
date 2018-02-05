#!/usr/bin/python
# coding:utf-8

import os

# 操作系统类型
print os.name
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 要获取详细的系统信息，可以调用uname()函数：
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# print os.uname()
print dir(os)

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print os.environ
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print os.environ.get('PATH')

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# 查看当前目录的绝对路径:
print os.path.abspath('.')
# 'D:\htdocs\python\lxf'
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2
print os.path.join('D:\htdocs\python\lxf', 'testdir')
# 'D:\htdocs\python\lxf\testdir'
# # 然后创建一个目录:
# os.mkdir('./testdir')
# 删掉一个目录:
# os.rmdir('./testdir')
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print os.path.split('./testdir/file.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 对文件重命名:
# os.rename('./testdir/file.txt', './testdir/file.py')
# 删掉文件:
# os.remove('./testdir/file.py')



