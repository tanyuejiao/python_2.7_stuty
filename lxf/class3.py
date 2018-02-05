#!/usr/bin/python
# coding:utf-8


class Student(object):
    name = 'Student'
    a = 1
    a = a+1

s = Student() # 创建实例s
s2 = Student() # 创建实例s2
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
print(Student.name) # 打印类的name属性
# Student
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student
print s.a
print s2.a
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：


class Student1(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student1.count += 1
        print(self.count)


# 测试:
if Student1.count != 0:
    print('测试失败!')
else:
    bart = Student1('Bart')
    if Student1.count != 1:
        print('测试失败!')
    else:
        lisa = Student1('Bart')
        if Student1.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student1.count)
            print('测试通过!')

