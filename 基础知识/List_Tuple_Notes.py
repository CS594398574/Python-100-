#-*-coding:utf-8-*-
"""
列表和元组：
    列表是动态的，可随意增加，删减或者改变，性能略微逊于元组。
    元组是静态的，无法改变，性能稍优

列表元组的使用场景：
    相同元素下，创建元组比列表更快，更轻量级。
    1、如果存储的数据和数量不变，选择元组更合适。比如有一个函数，返回一个地点的经纬度，然后直接传给前端渲染，元组更合适。
    2、如果存储的数据或者数量改变，比如社交平台查看日志功能，统计一个用户在一周内看到的帖子，则用列表更合适。

思考题：
A: empty_list = list()
B: empty_list = []
A、B这两种方式那种更优？
答案是B。
A，list()是一个funcation call，python的funcation call 会创建stack，并且进行一系列参数检查和操作，需要花费的开销更大
B,[]是一个内置的C函数，可以直接被调用，因此效率更高。
"""

l = [1,2,"hello",'world']
tup = ('jason',2)
print(l)
print(tup)
print(l[-1])    #列表和元组支持负数索引
print(tup[-1])
print(l[1:3])  #列表和元组支持切片操作
print(tup[0:])

l = [[1,2,4],[2,4,8]]           #支持随意嵌套
tup = ((1,2,3),(2,4,5))         #
print(l)
print(tup)

print(list(tup))                #list()和tuple()函数互相转换
print(tuple(l))

l = [3,2,3,7,8,9,0]
tup = (1,9,3,8,5,4)
print(l.count(3))           #count(item)计算列表/元组 中item出现次数
print(l.index(3))           #index(item)计算列表/元组 中item出现次数
print(l)
l.reverse()                 #原地倒转，元组没有这个函数
print(l)
l.sort()                    #表示对列表排序
print(l)

reversed(tup)              # reversed，sorted函数对list.tuple进行翻转和排序
sorted(tup)
print(tup)
print(tup)


#思考题
import timeit
print(timeit.timeit('a=list()',number=100000))
print(timeit.timeit('a=[]',number=100000))