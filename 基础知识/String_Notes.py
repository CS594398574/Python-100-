#-*-coding:utf-8-*-
"""
#字符串：是由独立字符组成的一个序列。 python 可以用(单引号，双引号，三引号），通常都一样三引号一般用于多行字符串场景，比如函数的注释

字符串拼接：
1、 +=
str1 += str2，每次处理字符串拼接操作，python首先检测str1还有没有其他引用，如没有就会原地扩充字符串buffer大小，
并不会重新分配内存来创建新字符串并拷贝，这样时间复杂度就比重新分配内存并拷贝方式低。做字符串拼接时，效率可以提高。
2、string.join(iterable) 使用字符串内置的join函数把每个元素都按照指定格式连接起来
L = [1,2,3,4,5]
L = ''.join(L)  L：12345

字符串分割:
string.split(separator)  表示字符串按照separator分割成子字符串且返回一个子字符串组合的列表
运用场景：对数据的解析处理，如读取某个文件想要调用数据库的API，去读取对应的数据例子见代码块

string.strip(str)  去掉首尾的str字符串  ，不填str则默认是空字符。下面函数类似
string.lstrip(str) 去掉开头的str字符串
string.rstrip(str) 去掉尾部的str字符串

字符串格式化
print('....{}..{}'.format(x,y))
运用场景：通常在输出、日志的记录方面


思考题：  以下AB两种拼接方式，那个更优？

Option ：A
s = ''
for n in range(0,10000)
    s += str(n)

Option: B
l = []
for n in range(0,10000)
    l.append(str(n))
s.''.join(l)

答案：
如果字符串拼接较少;比如range(100),A方法更优，因为时间复杂度来讲精确的说，A是o(n),B是o(2n).
但是如果range(1000000),方法二稍微快点，虽然遍历两次，但是join速度其实很快，列表append()函数和join的开销要比字符串+=小一些。

"""

#字符串常用操作
name = "jason"
print(name[0])   #可以索引
print(name[0:3])
for char in name:  #遍历
    print(char)

#字符串不可变
s = 'hello'
#s[0] = 'H'   #不被允许
#改变字符串只能通过创建新的字符串完成
s = 'H' + s[1:]         #通过'+'操作符，拼接原子串。
s = s.replace('h','H') #通过扫描原字符串，将'h'替换成大写'H'   note:其他的语言有可变字符串，如java，使用StringBuilder，无需创建新的字符串。
#print(s)

# ’+= '字符串拼接方法。打破了字符串不可变的特性。  重点
s = ''
for n in range(0,100000):
    s += str(n)                 # 创建buffer，不会重新分配空间拷贝字符. 时间复杂度为o(n)
#print(s)
l = []
for n in range(0,100000):
    l.append(str(n))           #append()操作是o(1)复杂度 l=['0','1','2'.....'100000'] 有引号，是字符串类型
l = ''.join(l)                #时间复杂度为o(n)
#print(l)


#字符串分割
def query_data(namesapce,table):
    """
    given namesapce and table,query database to get corresponding
    :param namesapce:
    :param table:
    :return:
    """
path = 'hive://ads/training_table'
namesapce = path.split("//")[1].split('/')[0]
print(namesapce)   #return ads
table = path.split("//")[1].split("/")[1]
print(table)      #return training_table
#data  = query_data(namesapce,table)

s = ' my name is jason '
print(s.strip()) #去掉首尾空格
print(s.lstrip()) #去掉开头str字符串，这里str默认是空，即是空字符
print(s.rsplit('is'))  #return [' my name ', ' jason ']
print(s.rsplit('is')[0]) #return  my name ,my name左右都有一个空格

#字符串格式化
id = "01"
print("....{}......{}".format(id,name))

#思考题coding测试
import time
start_time = time.perf_counter()            #time.perf_counter()返回性能计时器的值
s = ''
for n in range(0, 1000000):
    s += str(n)                             # 创建buffer，不会重新分配空间拷贝字符. 时间复杂度为o(n)
end_time = time.perf_counter()
print("Option A need time:{}".format(end_time - start_time))

start_time = time.perf_counter()            #time.perf_counter()返回性能计时器的值
l = []
for n in range(0,1000000):
    l.append(str(n))           #append()操作是o(1)复杂度 l=['0','1','2'.....'100000'] 有引号，是字符串类型
l = ''.join(l)
end_time = time.perf_counter()
print("Option B need time:{}".format(end_time - start_time))

#Option C:更优的一种拼接方式
start_time = time.perf_counter()
s = ''.join(map(str,range(0,1000000)))
end_time = time.perf_counter()
print("Option C time elapse:{}".format(end_time- start_time))
