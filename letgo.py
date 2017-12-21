# import sys
# for i in sys.path:
#     print(i)
#
# ilist=[1,2,3,4,5,6]
# print(enumerate(ilist))
# print(list(enumerate(ilist,1)))
# # print(enumerate.__doc__)

# info={'name':'MimuTao','age':24}
# ret=info.setdefault('school','zhejang university')
# print(info)
# print(ret)
# print(dict.setdefault.__doc__)

# from collections import defaultdict
# info = defaultdict(int)
# list = ['python', 'python', 'rust', 'go']
# for item in list:
#     info[item] += 1
#
# print(dict(info))
#
# print(defaultdict.__doc__)

# from collections import deque
# print(deque.__doc__)
# deq=deque([x for x in range(10)])
# for i in range(10):
#     print(list(deq.copy()))

# list1=[1,2,3,4]
# list2=list1[::-1]
# print(list1 ==list2[::-1])
# print(list2)
# from pprint import pprint
# info ={'name':'lenus','age':23}
# pprint(info)

# num=7
# print(type(num))

class base():
    def __init__(self,name):
        self.__name=name
        base.__count+=1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name

    @staticmethod
    def imessage(word):
        print(word)

    __count=0
    @classmethod
    def count(cls):
        return cls.__count

# base.imessage('hello')
# print(base.count())

# a=base('iq')
# b=base('cq')
# print(base.count())


# from collections import Counter
# isa=Counter(['make','make','jack'])
# print(dict(isa))

# from collections import namedtuple
# Human=namedtuple('Human','name age')
# instance=Human('zhangming',13)
# print(instance)
# print(instance.name)
# another_ins=instance._replace(name='liming')
# print(another_ins)
# t_instance=Human(name='wangli',age=15)
# print(t_instance)
# print(t_instance._fields)
# iname=getattr(t_instance,'name')
# print(iname)
#
#
#
# class temp():
#     def __str__(self):
#         return temp.__name__+ 'hahaha'
#
#
# data=temp()
# print(data)

# import re
# mail='taoyueyue54@qq.com'
# result=re.match(r'^[a-zA-Z]\w*@\w+.[a-z]{2,4}',mail)
# # result=re.search('h.*?n','hi,my name is tyy and you can hit me in the hidden hitter.')
# if result:
#     print(result.group())
# else:
#     print('not found\n')

# result=re.findall('h\w*n','hi,my name is tyy and you can tell me your name. hidden info can find by hit the buttom.')
# print(result)

# usa_match=re.match('^(\(\s*\d{3}\s*\)|\d{3})-?\d{3}-\d{4}','(555)555-1234')
# zju_mail=re.match('^\w{4,}@zju.edu.cn','21732asdfadfae__qt23424gagadgaqag013@zju.edu.cn')
# if zju_mail:
#     print(zju_mail.group())
# else:
#     print('not found.')
# if usa_match:
#     print(usa_match.group())
# else:
#     print('not found.')

# identication=re.match('\d{17}(\d|\*)','12345678912345678*')
# if identication:
#     print('identication:',identication.group())
# else:
#     print('not match.')

# print(re.findall(r'\b[abc][a-z]*b\b','cello art you ok babe aob cob'))

# print(re.split('\s+|_','first of    all_it\'s important'))

import csv
# data=[
#     ['yyt','first'],
#     ['mue.lt','second'],
#     ['lenus','thrid']
# ]
# with open('csvfile','wt') as file:
#     csvout=csv.writer(file)
#     csvout.writerows(data)
# with open('csvfile','rt') as file:
#     cin=csv.reader(file)
#     data=[row for row in cin] 

# for i in data:
#     print(i)

import sqlite3

conn= sqlite3.connect('info.db')
cursor=conn.cursor()


# cursor.execute('CREATE TABLE user(id int PRIMARY KEY NOT NULL, name char[50], age INT)')
# cursor.execute('INSERT INTO user(id,name,age) VALUES (1,"zhangsan",24)')
# cursor.execute('INSERT INTO user (id,name,age) VALUES (?,?,?)',(2,"lisi",23))
# cursor.execute('INSERT INTO user(id,name,age) VALUES (3,"xiaoge",18)')
# print(cursor.rowcount)
cursor.execute('SELECT * FROM user WHERE id =?',(3,))
result=cursor.fetchall()
print(result)

# cursor.execute('INSERT INTO user (id,name) VALUES (5,"mue_lt")')
cursor.execute('SELECT * FROM user')
result=cursor.fetchall()
print(result)

result=cursor.execute('select sum("id") as average from user where id>=3')
result=cursor.fetchone()
print(result[0])

cursor.execute(r'UPDATE user SET age= 24 WHERE id IS 6')
cursor.execute('SELECT * FROM user WHERE id =6')
result=cursor.fetchone()
print(result)

# cursor.execute('''CREATE TABLE books(
#                     book_id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
#                     name varchar(255) NOT NULL
#                 )
#                 ''')
# cursor.execute('DROP TABLE books')

# cursor.execute('INSERT INTO books(name) VALUES (?)',('Procrastination',))
cursor.execute('SELECT * FROM books WHERE name LIKE "%ha%"')
result=cursor.fetchall()
print(result)

# cursor.close()
# conn.commit()
# conn.close()