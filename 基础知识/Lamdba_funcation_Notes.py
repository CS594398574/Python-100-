from functools import reduce

"""
简约而不简单的：匿名函数：lambda。
lambda: arguments1,arguments2,....argumentN:expresision
        参数:表达式

1、lambda： 是一个表达式，并不是一个语句。
表达式：就是用一系列“公式”表达一个东西，比如：x+2,x**2;
语句:  赋值语句： x =1.   print()语句,条件语句等等。
因此lambad可以用在列表内部    [(lambda x:x*x)(x) for x in range(10)]
lambad可以作某些函数的参数
2、lambda：函数主题是只有一行简单的表达式，并不能扩展成一个多行的代码块

python函数式编程
函数式编程，指代码中每一块都不可变，都由纯函数的形式组成。纯函数是指函数互相独立，互不影响。
纯函数优点在于不可变性让程序更加健壮，容易调试。

map(function,iteralble)表示iterable中的每个元素，都运用在funcation这个函数中，最后返回一个新的可遍历的集合。
filter(function,iterable)函数，与map函数类似，function同样表示一个函数对象，filter()函数表示对iterable中每个元素都是用funcation判断，返回true或者false。
最后将返回True的元素组成一个新的可遍历的集合。
 
匿名函数使用场景：
程序中需要使用一个函数完成一个简单的功能，并且该函数只调用一次。

"""
squre = lambda x:x**2
def squre1(x):
    return x**2
print(squre(3))  #匿名函数
print(squre1(3)) #常规函数

#用在列表内部的lambda函数
print([(lambda x:x*x)(x) for x in range(10)])   #[0~9]平方

l = [(1,20),(3,0),(9,10),(2,-1)]
l.sort(key=lambda x:x[1]) #按列表中第二个元素排序
print(l)

#对列表中所有元素做平方操作
l = [1,2,3,4,5]
squre = list(map(lambda x:x**2,l))
print()
print(squre)

#函数式编程sample
#1、非函数式编程
def multipley_2(l):
    for index in range(0,len(l)):
        l[index] *=2
    return l
#该代码，每次运行，列表中的函数值会被改变，多次调用后，每次得到结果都不一样
#2、函数式编程
def multiply_20(l):
    new_list = []
    for item in l:
        new_list.append(item*2)
    return new_list

a = [1,2,3,4,5,6]
b = [5,4,3,2,1]
print('a',a)
print('b',b)
multipley_2(a)
multiply_20(b)
print(a)
print(b)

#map(),filter(),reduce()结合lambda一起使用

#map funcation:   map(function,iteralble)表示iterable中的每个元素，都运用在funcation这个函数中，最后返回一个新的可遍历的集合。
l =[1,2,3,4,5]
new_list = map(lambda x:x*2,l)
print(list(new_list))
print(l)

#filter(funcation,iterable)
l =[1,2,3,4,5,6]
new_list = filter(lambda x:x%2==0,l)
print(list(new_list))
print(l)

#reduce(funcation,iterable)函数。          对iterable数组中一般用funcation进行一些累积操作。
l = [1,2,3,4,5]
product = reduce(lambda x,y:x*y ,l)
print(product)

d ={'mike':10,'lucy':2,'ben':30}
d_sort_key = sorted(d.items(),key=lambda x:x[1],reverse=False) #reverse=False是升序，reverse=True是降序返回一个值。
print(d_sort_key)
for key,value in d.items():
    print(key,value)
