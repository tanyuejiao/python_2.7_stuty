#!/usr/bin/python
# coding:utf-8

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        # continue的作用是提前结束本轮循环，并直接开始下一轮循环。
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
