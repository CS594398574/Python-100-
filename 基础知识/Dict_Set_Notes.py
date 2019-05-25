#-*-coding:utf-8-*-
"""
python中字典和集合，无论是键还是值，都可以是混合类型。
字典支持索引操作，可以通过dict(['key'])或者dic.get('key')来访问value的值
集合不支持索引操作，其本质上是一个哈希表，和列表不一样。

字典和集合具有高效性，特别是对于查找、插入和删除操作。
之所以如此高效，因为字典和集合的内部结构都是一个张哈希表
字典：该表存储哈希值（hash）、键和值3个元素
集合：区别是哈希表没有键和值的配对，只有单一的元素

字典集合运用场景：对元素的高效查找、去重。
思考题：
1、
d ={'name':'jason','age':20,'gender':'male'} #A
d = dict({'name':'jason','age':20,'gender':'male'}) #B
那个更高效？
答案是A。    B方式是是一个function call。需要创建stack，且检查参数合法性等操作，开销更大
2、
d = {'name':'jason',['education']:['Tsinghua University','Stanford Unveristy']} 初始化是否正确？

不正确，列表作为key是不被允许。字典键值不可变，而列表是动态的,可变的，此处可以元组替换列表。
"""
#1.创建和访问
#字典创建方式
d1 = {'name':'jason','age':20,'gender':'male'}
d2 = dict({'name':'jason','age':20,'gender':'male'})
d3 = dict([('name','jason'),('age',20),('gender','male')])
d4 = dict(name='jason',age=20,gender='male')
print(d1==d2==d3)
#Set的创建方式
s1 = {1,2,3}
s2 = set([1,2,3])
print(s1==s2)
#都可以混合搭配
s = {1,'hello',5.0}
print(s)

#元素访问,字典可以通过Key（也就是索引键）访问
d = {'name':'jason','age':20}
print(d['name'])    #使用[ ]访问
#print(d['location'])   #字典key索引不存在，会报错
print(d.get('name'))  #使用get函数进行索引访问，get函数可以有一个默认值，当字典不存在则会返回null
print(d.get("location"))  #字典key索引不存在，会返回一个null

#集合不支持索引，所以不能用s[0]来访问元素
s = {1,2,3}
#print(s[0])   报错。
#判断一个元素是否在集合或者字典中value in dict/set
print(1 in s)           #判断一个元素是否在集合中,利用value in set来判断
print('name' in d)

#2.增加、删除、更新等操作
#字典更新操作
d = {'name':'jason','age':20}
d['gender'] = 'male'      #增加元素对 'gender':'male'
d['bob'] = '1999-02-02'
print(d)
d['bob'] = '1999-01-04' #更新
print(d)
d.pop('gender')    #删除
print(d)
#集合更新操作
s = {0,1,2,3,8}
s.add(4)
print(s)
s.remove(4)
print(s)
s.pop()     #该操作是删除集合最后一个元素，集合本身无序，无法知道删除那个元素，所以慎用
print(s)


#排序，例子，比如你要取出值最大的50对
#字典，本身无序
d = {'b':1,'a':2,'c':10}
d_sort_by_key = sorted(d.items(),key=lambda  x:x[0])   #根据字典键值升序排序
d_sort_by_value = sorted(d.items(),key=lambda x:x[1])  #根据字典值的升序排序
print(d_sort_by_key)
print(d_sort_by_value)
#集合
s = {3,4,2,1}
print(sorted(s))  #sorted()排序

#字典和集合性能
#字典和结合进行过性能高度优化的数据结构 尤其是查找，添加和删除操作
#与列表数据结构做对比
#例子：电商后台存储，产品ID、名称、价格。需求：给定ID找出价格

#列表存储id和price
def find_product_price(products,product_id):
    for id,price in products:
        if id == product_id:
            return price
    return None
products =[(12345,100),
           (23456,30),
           (34567,150)]
print("The price of product 12345 is {}".format(find_product_price(products,12345)))

#字典存储
products={
    12345:100,
    23456:30,
    34567:150
}
print("The price of product 12345 is {}".format(products[12345]))   #直接通过键的哈希值知道相应的值。

#如果需求变成找出这些商品有多少种不同的price，依然使用list，下面代码#A，#B是两个循环，因此需要O(n^2)的时间复杂度
#list version:
def find_unique_price_using_list(products):
    unique_price_list = []
    for _,price in products:  #A
        if price not in unique_price_list: #B
            unique_price_list.append(price)
    return len(unique_price_list)
products = [
    (12345,100),
    (23456,30),
    (34567,150),
    (45678,30)
]
print('number of unique price is {}'.format(find_unique_price_using_list(products)))

#如果是使用set，集合是高度优化的哈希表，里面元素不可以重复，并且添加和查找操作只需o(1)复杂度，总时间复杂度就只有o(n)
#set version:
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _,price in products:
        unique_price_set.add(price)
    return len(unique_price_set)
products = [
    (12345,100),
    (23456,30),
    (34567,150),
    (45678,30)
]
print('number of unique price is {}'.format(find_unique_price_using_set(products)))

#所以时间复杂度set更优
#为了更直观的了解时间复杂度，我们通过100,000个元素产品举例子

import time
id = [x for x in range(0,100000)]
price = [x for x in range(200000,300000)]
products = list(zip(id,price))
print(len(products))

#计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list:{}".format(end_using_list - start_using_list))
#结果是：time elapse using list:40.69249
#计算集合版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_set(products)
end_using_list = time.perf_counter()
print("time elapse using list:{}".format(end_using_list - start_using_list))
#结果是：time elapse using list:0.009066700000005312
#可以看到当用户数量级增加到十万时，两者速度差异就非常大。
d = {'name':'jason',('education'):['Tsinghua University','Stanford Unveristy']}
print(d)