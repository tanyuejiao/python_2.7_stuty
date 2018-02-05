#!/usr/bin/python
# coding:utf-8


# def log(func):
#     print 1
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# # @log
# # def now():
# #     print('2015-3-25')
# #
# # now()
#
# def test(x, y):
#     print "test"
#
#     def test1():
#         print x + y
#     return test1
#
# f1 = test(1, 2)
# print "f1:", f1
# f2 = log(f1)
# print "f2:", f2
# f2()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')
now()