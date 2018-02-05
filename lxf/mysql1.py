#!/usr/bin/python
# coding:utf-8

########## prepare ##########

import MySQLdb

# 打开数据库连接
# 通常我们在连接MySQL时传入use_unicode=True，让MySQL的DB-API始终返回Unicode。
conn = MySQLdb.connect("127.0.0.1", "root", "", "test")

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', '谭岳姣'])
# cursor.execute('insert into user (id, name) values (%s, %s)', ['3', '谭岳姣'])
print "行数为：", cursor.rowcount
# 1
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s and name = %s', ('3', "谭岳姣") )
values = cursor.fetchall()
print values
# [(u'1', u'Michael')]
# 关闭Cursor和Connection:
cursor.close()
# True
conn.close()