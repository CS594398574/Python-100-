#-*-coding:utf-8-*-
"""
一、从内存输入或者输出
1、input("提示语")暂停程序运行，等待键盘输入,函数参数为提示语.输入类型永远是字符串类型(str)
2、print()函数接受字符串、数字、字典、列表甚至一些自定义的输出；python对int没有最大限制，C++中对int有限制比如2147483647， 但是对float类型依然有精度限制。

二、从外部文件输入或者输出
with open(1，2) as f:
第1参数表示文件位置，相对位置或者绝对位置。
第2参数，‘r':读取。'w':写入。'rw'：读写。'a'：追加，打开文件如果需要写入，则会从末尾开始加入。
利用open( )函数拿到文件的指针,通过read函数来读取文件所有内容。将文件所有内容读取到内存。
read()优点是方便调用我们写的解析函数。缺点是文件过大，一次性读取可能会造成内存崩溃。
可以指定read(size)或者用readline() 降低内存压力。

三、JSON序列化与实战
JSON：一种轻量级数据交换格式。
运用场景：当数据中包含字符串、整数、浮点数、bool类型混合在一起时，则可以用JSON处理。
场景使用理解：
1、输入这些杂七杂八的信息，如python字典，输出一个字符串
2、输入这个字符串，可以包含原始信息python字典。
json.dumps()，结束python的基本数据类型，然后将其序列化成string
json.loads(),接受合法字符串，将其反序列话为python基本数据类型
当开发一个第三方应用程序时，可以通过json文件将用户的个人配置输出到文件，方便下次程序启动时自动读取。

四：思考题
A：你能否把 NLP 例子中的 word count 实现一遍？不过这次，in.txt 可能非常非常大（意味着你不能一次读取到内存中），
而 output.txt 不会很大（意味着重复的单词数量很多）。提示：你可能需要每次读取一定长度的字符串，进行处理，然后再读取下一次的。
但是如果单纯按照长度划分，你可能会把一个单词隔断开，所以需要细心处理这种边界情况。

B：你应该使用过类似百度网盘、Dropbox 等网盘，但是它们可能空间有限（比如 5GB）。
如果有一天，你计划把家里的 100GB 数据传送到公司，可惜你没带 U 盘，于是你想了一个主意：
每次从家里向 Dropbox 网盘写入不超过 5GB 的数据，而公司电脑一旦侦测到新数据，就立即拷贝到本地，然后删除网盘上的数据。
等家里电脑侦测到本次数据全部传入公司电脑后，再进行下一次写入，直到所有数据都传输过去。
根据这个想法，你计划在家写一个 server.py，在公司写一个 client.py 来实现这个需求。
提示：我们假设每个文件都不超过 5GB。
你可以通过写入一个控制文件（config.json）来同步状态。不过，要小心设计状态，这里有可能产生 race condition。
你也可以通过直接侦测文件是否产生，或者是否被删除来同步状态，这是最简单的做法。

思考题解析放末尾：
"""






#键盘输入  input()
# name = input("your name")  #输入永远是字符串类型
# #print("your name:{}".format(name))
# gender = input('youare a boy?(y/n)')
# #print("boy?{}".format(gender))
# welcome_str = "Welcome to the matrix {prefix} {name}"
# welcome_dic = {
#     'prefix':'Mr.' if gender == 'y'or'yes'or'Y'or'Yes' else 'Mrs.',
#     'name':name
# }
# print('authorizing..........')
# print(welcome_str.format(**welcome_dic))

#input输入类型是字符型
# a = input()
# b = input()
# print("a+b={}".format(a+b)) #ab做拼接

#一个简单的NLP任务：
"""
1、读取文件
2、去除所有标点符号和换行符，并把所有大写变成小写
3、合并相同的词，统计每个词出现的频率，并且按照词频从大到小排序
4、将结果按行输出到out.txt
"""
import re

def parse(text):                         #解析统计txt文本词频出现的次数函数
    text = re.sub(r'[^\w]',' ',text)   #用正则表达式出去标点符号和换行符号
    text = text.lower()                 #将所有大写转换成小写
    word_list = text.split(' ')         #生成所有单词列表
    word_list = filter(None,word_list)  #取出空白单词

    #生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    #按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(),key=lambda kv:kv[1],reverse=True)
    return sorted_word_cnt

with open('./Data/in.txt','r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('./Data/out.txt','w') as fout:
    for word,feq in word_and_freq:
        fout.write('{} {}\n'.format(word,feq))


word_and_freq = parse(text)
#print(word_and_freq)

#JSON使用实例
import json

#例子，将python基本类型数据结构params数据序列化成string，然后再将stirng反序列化成字典数据类型。
params ={
    'symbol':'123456',
    'type':'limit',
    'price':123.5,
    'amount':23
}
params_str = json.dumps(params)
print("after jason serialization")
print('type of params_str ={},params_str={}'.format(type(params_str),params))
#type of params_str =<class 'str'>,  params_str={'symbol': '123456', 'type': 'limit', 'price': 123.5, 'amount': 23}
original_parms = json.loads(params_str)
print("after json desrizliaztion")
print("type of original_params = {},original_params ={}".format(type(original_parms),original_parms))

#将字符串读取/输出到内存，再进行JSON编码/解码。
params ={
    'symbol':'123456',
    'type':'limit',
    'price':123.5,
    'amount':23
}
with open('./Data/params.json','w') as fout:
    params_str = json.dump(params,fout)

with open('./Data/params.json','r') as fin:
    original_parms = json.load(fin)

print("after json deserialization")
print("type of original_params = {},original_params ={}".format(type(original_parms),original_parms))





#思考题解析：
#思考题A:
import re
CHUNK_SIZE = 100
def parse2(text,last_word,word_list):                         #解析统计txt文本词频出现的次数函数
    text = re.sub(r'[^\w]',' ',text)   #用正则表达式出去标点符号和换行符号
    text = text.lower()                 #将所有大写转换成小写
    cur_word_list = text.split(' ')         #生成所有单词列表
    cur_word_list,last_word = cur_word_list[:-1],cur_word_list[-1]
    word_list += filter(None,cur_word_list)   #filter(None,cur_word_list),可以过滤掉空值，且能够过滤0，None，空列表等值
    return last_word

def solve():
    with open('./Data/in.txt','r') as fin:
        word_list,last_word =[],''
        while True:
            text = fin.read(CHUNK_SIZE)
            if not text:
                break #读取完毕，中断
            last_word = parse2(text,last_word,word_list)

        word_cnt ={}
        for word in word_list:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1
        sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_word_cnt
print(solve())

#思考题B：
#server.py     server所有文件都在BASR_DIR,网盘路径在NET_DIR

import os
from shutil import copyfile
import time 

BASE_DIR = '/server/'
NET_DIR = 'net/'

def main():
    filenames = os.listdir(BASE_DIR)
    for i,filename in enumerate(filenames):
        print("copying {} into net drive...{}/{}".format(filename,i+1,len(filenames)))
        copyfile(BASE_DIR + filename,NET_DIR + filename)
        print("copied {} int net drive,waiting client complete...{}/{}".format(filename,i+1,len(filenames)))
        
        while os.path.exists(NET_DIR+filename):
            time.sleep(3)
        print("transferred {} int client.{}/{}".format(filename,i+1,len(filenames)))

if __name__ == "__main__":
    main()

#client.py
import os
from shutil import copyfile
import time 

BASE_DIR = '/client/'
NET_DIR = 'net/'

def main():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print("downloading {}into local disk.....".format(filename))
            copyfile(NET_DIR + filename,BASE_DIR + filename)
            os.remove(NET_DIR+filename)  #删除该文件，网盘同步，server知晓完成
            print("downloaded{} into local disk.".format(filename))
            time.sleep(3)

if __name__ == "__main__":
    main()
