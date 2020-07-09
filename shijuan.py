# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:01:39 2019

@author: XURONGZHONG641
"""
import random
import shutil
import os

selects = [
    ('''找出所有购入商品为两种或两种以上的name的订单记录

预期结果：

+----+------+---------+--------+
| id | name | product | number |
+----+------+---------+--------+
|  1 | A    | pen     | 2      |
|  2 | B    | hat     | 4      |
|  3 | C    | car     | 1      |
|  4 | A    | book    | 2      |
|  5 | B    | pen     | 5      |
|  6 | A    | pen     | 5      |
|  8 | C    | pencil  | 1      |
|  9 | A    | book    | 2      |
| 10 | B    | pen     | 2      |
+----+------+---------+--------+

''', 
'''select * from orders where name in (select name from orders group by name having count(*) >= 2);'''),
         
    ('''找出购买数number都大于3的name的订单
预期结果
+----+------+---------+--------+
| id | name | product | number |
+----+------+---------+--------+
|  7 | E    | apple   | 4      |
+----+------+---------+--------+

    
''', 

'''select * from orders where name not in (select distinct name from orders where number < 3);
或者：
select * from orders where name in (select name from orders group by name having min(number) >=3);'''),
    
    ('''找出平均每单number大于3的产品名称：
     
预期结果
+---------+
| product |
+---------+
| pen     |
| hat     |
| apple   |
+---------+

''',  
'''select product from orders group by product having avg(number) > 3;'''),
     
    ('''选择产品名product为c-z开头的行(注意产品名还有一些是_或中文等开头的)。：
     
预期结果
+----+------+---------+--------+
| id | name | product | number |
+----+------+---------+--------+
|  1 | A    | pen     | 2      |
|  2 | B    | hat     | 4      |
|  3 | C    | car     | 1      |
|  5 | B    | pen     | 5      |
|  6 | A    | pen     | 5      |
|  8 | C    | pencil  | 1      |
| 10 | B    | pen     | 2      |
+----+------+---------+--------+


''',  
'''SELECT * FROM orders WHERE product REGEXP '^[c-z]';'''),     
         
]
    
bianchens = [
    '''现在有文件test.txt
jason
jason
jason
fffff
jason
请使用linux命令、shell或python、java等进行去重，预期结果：
fffff
jason''',
    '''在以下文本中找出 每行中长度超过3的单词:
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick

python的预期结果(尽量不超过3行搞定):
    
[['Call', 'Ishmael.', 'Some', 'years', 'never', 'mind', 'long', 'precisely', 'having'], ['little', 'money', 'purse,', 'nothing', 'particular', 'interest'], ['shore,', 'thought', 'would', 'sail', 'about', 'little', 'watery', 'part'], ['world.', 'have', 'driving', 'spleen,', 'regulating'], ['circulation.', 'Moby', 'Dick']]]
    ''',
    '''请使用linux命令、shell或python、java等实现字符串反序，以python为例：
$ ./numbers.py 10572 
 
Reverse number is 27501''',
    '''请使用linux命令、shell或python、java等向http://httpbin.org/post，提交json '{"kew":"value"}' ''',
     '''请将当前目录的*py 重命名为*.pyc''',   
]
    
ceshidians = ["支付宝APP安卓端安全测试", "ubuntu 20.04安装mysql", "ubuntu 20.04使用cp拷贝目录"]

ceshis = [
    '请列出至少4种测试用例设计方法，并简介其使用场景',
    '如何发现内存泄露？',
    '常用的资源监控命令或方法有哪些？',
    '你的测试职业发展规划是？',  
    '性能测试需要关注哪些指标，请列出至少5个，并简述含义?列出3个你在性能测试中发现的问题。性能测试如果发现问题？'
    ]

if os.path.exists("shiti.txt"):
    shutil.copyfile("shiti.txt","shiti2.txt")

f = open("shiti.txt",'w')
description = '''欢迎参加平安产险数据平台测试组的面试！

本次考试共5道题，为后续工作强相关内容，每题1分， 总计5分，通过分为3分。
请在打印纸上作答。答题时间50分钟。
考试不能代表全部，如果您有其他方面的特长，请在后续面试充分展现自己，谢谢！ 
联系人 钉钉或微信 pythontesting 

1,SQL基础题

mysql> select * from myflixdb.orders;
+----+------+---------+--------+
| id | name | product | number |
+----+------+---------+--------+
|  1 | A    | pen     | 2      |
|  2 | B    | hat     | 4      |
|  3 | C    | car     | 1      |
|  4 | A    | book    | 2      |
|  5 | B    | pen     | 5      |
|  6 | A    | pen     | 5      |
|  7 | E    | apple   | 4      |
|  8 | C    | pencil  | 1      |
|  9 | A    | book    | 2      |
| 10 | B    | pen     | 2      |
...
+----+------+---------+--------+

'''
print(description)
f.write(description)
shiti = selects[random.randint(1,len(selects)-1)]
print(shiti[0])
f.write(shiti[0] + '\n')
print('\n')
print(shiti[1])

description = '\n\n2,编程题 -- 此题如能在本机(unbuntu)上调试出来更佳。\n'
print(description)
f.write(description)
shiti = bianchens[random.randint(1,len(bianchens)-1)]
print(shiti)
f.write(shiti + '\n')

description = '\n\n3,测试点设计: 请列出至少15个测试点\n'
print(description)
f.write(description)
shiti = ceshidians[random.randint(1,len(ceshidians)-1)]
print(shiti)
f.write(shiti + '\n')

description = '\n\n4,测试基础题\n'
print(description)
f.write(description)
shiti = ceshis[random.randint(1,len(ceshis)-1)]
print(shiti)
f.write(shiti + '\n')

description = '''
5.描述下你测试过产品的前后台架构，建议画图描述, 可以手写拍照
描述你在上述产品你发现的跨至少３个模块的bug，至少３个。
描述下你常去的国外的能解决问题的网站。
'''
print(description)
f.write(description)

description = '\n\n6.个人信息收集: \n优点\缺点\未来3年内的规划\现在月薪及年薪\要求的月薪及年薪\对加班怎么看\住所(主要看到公司有多远)请提出一些独到的测试想法，比如你近期申请过或准备申请的测试专利。\n'
print(description)
f.write(description)

f.close()
