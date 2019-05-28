#-*-coding:utf-8-*-
"""
本实验环境在 python 2.7测试
条件循环：
遍历字典：字典本身只有键值可以迭代，如果要遍历键值或者键值对，则遍历values或者items()

range(),拿到索引，再遍历访问集合中的元素。  range()函数直接由C语言写，调用速度非常快。
同时需要索引和元素时候，可用enumerate()遍历集合，返回元素和索引

for:while()使用场景：
遍历一个集合，找出满足条件的元素。用for更简洁。
需要满足某个条件，不停重复操作，么有特定集合需要遍历，用while


expression if condition else expression2 for item in iterable
== for item in iterable
    if condition:
        expresion1
    else:
        expresion2
没有else则写成：
expression for item in iterable if condition

思考题：
给定两个列表转换成字典：
attributes = ['name','dob','gender']

values = [['jason','2000-01-01','male'],
          ['mike','1999-01-01','male'],
          ['nancy','2001-02-01','famale']]
方法一：
for i in range(0,len(values)):
    dict_cacach = {}
    for j in range(0,len(values[0])):
        dict_cacach[attributes[j]] = values[i][j]
    list_dict.append(dict_cacach)
for i in range(0,len(list_dict)):
    print list_dict[i]
方法二：
lists = [dict(zip(attributes,v) for v in values)]
zip()函数直接将v中的元素和attributes中元素一一打包成元组列表。

注意：
[('name','nancy')] 可以直接初始化成字典键值对
dict(list(tuple("",""))) 直接键值对化
"""

#遍历列表
l = [1,2,3,4]
for item in l:
    print item

#遍历字典
d = {'name':'jason','dob':'2000-01-01','gender':"male"}

for k in d:         #遍历键
    print k

for v in d.values():   #遍历键值
    print v

for k,v in d.items():  #遍历键值对
    print k,v

l = [1,2,3,4,5,6,7]
for index in range(0,len(l)):  #range()获取索引
    if index<5:
        print l[index]

for index,item in enumerate(l):  #enumerate()可以同时获取索引和元素
    if index<5:
        print index,item

color_price = {  'red':100,
                   'white':200,
                   'blue':300,
                   'green':400,
                   }
namecolor = [
    'red','white','blue'
]
for name,price in color_price.items():
    print name,price
    if price >1000:
        continue
    if name not in namecolor:
        print('name:{},color:{}'.format(name,'None'))
        continue


x = [1,2,3,4,5,6,7]
y = [value *2 +5 if value>0 else -value*2+5 for value in x]
print y

text = 'today, is, Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip())>3]  #去掉首位空字符，并过滤掉长度小于3的单词。
print text_list

attributes = ['name','dob','gender']

values = [['jason','2000-01-01','male'],
          ['mike','1999-01-01','male'],
          ['nancy','2001-02-01','famale']]

list_dict =[]


print"------------------------"
for i in range(0,len(values)):
    dict_cacach = {}
    for j in range(0,len(values[0])):
        dict_cacach[attributes[j]] = values[i][j]
    list_dict.append(dict_cacach)
for i in range(0,len(list_dict)):
    print list_dict[i]
print"________________________"
for v in values:
    ss = zip(attributes,v)
    print ss
    s = dict(zip(attributes,v))
    print s


lists = [dict(zip(attributes,v) for v in values)]
# print lists

tup = [('name','nancy')]
dictss = dict(tup)
print dictss
