# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:01:39 2019

@author: XURONGZHONG641
"""
import random
import shutil
import os

selects = [
    ('''在OrderItems表找出所有prod_id为4种或以上的prod_id记录

预期结果：

+-----------+------------+---------+----------+------------+
| order_num | order_item | prod_id | quantity | item_price |
+-----------+------------+---------+----------+------------+
|     20005 |          2 | BR03    |      100 |      10.99 |
|     20006 |          3 | BR03    |       10 |      11.99 |
|     20007 |          1 | BR03    |       50 |      11.49 |
|     20008 |          2 | BR03    |        5 |      11.99 |
+-----------+------------+---------+----------+------------+
''', 
'''
select * from OrderItems where prod_id in (select prod_id from OrderItems group by prod_id having count(*) >= 4);
'''),
         
    ('''选择OrderItems表中产品价格(prod_price)r都大于等于9的供应商(vend_id)的订单
预期结果
+---------+---------+------------+------------+--------------------------------------------------+
| prod_id | vend_id | prod_name  | prod_price | prod_desc                                        |
+---------+---------+------------+------------+--------------------------------------------------+
| RYL01   | FNG01   | King doll  |       9.49 | 12 inch king doll with royal garments and crown  |
| RYL02   | FNG01   | Queen doll |       9.49 | 12 inch queen doll with royal garments and crown |
+---------+---------+------------+------------+--------------------------------------------------+


    
''', 

'''
select * from Products where vend_id not in (select distinct vend_id from Products where prod_price < 9);
或者：
select * from Products where vend_id in (select vend_id from Products group by vend_id having min(prod_price) >=9);
'''),
    

     
    ('''选择OrderItems表中产品名prod_id为C-Z开头的行(注意prod_id还有一些是_或中文等开头的)。：
     
预期结果
+-----------+------------+---------+----------+------------+
| order_num | order_item | prod_id | quantity | item_price |
+-----------+------------+---------+----------+------------+
|     20007 |          5 | RGAN01  |       50 |       4.49 |
|     20008 |          1 | RGAN01  |        5 |       4.99 |
+-----------+------------+---------+----------+------------+

''',  
'''
SELECT * FROM OrderItems WHERE prod_id REGEXP '^[c-z]';
'''),     
     
    ('''基于Products表，列出具有两个以上价格（prod_price）大于等于4产品的供应商(vend_id)及产品数:。
     
预期结果
+---------+-----------+
| vend_id | num_prods |
+---------+-----------+
| BRS01   |         3 |
| FNG01   |         2 |
+---------+-----------+


''',  
'''
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
WHERE prod_price >= 4
GROUP BY vend_id
HAVING COUNT(*) >= 2;
'''),       
         
    ('''基于表OrderItems, Products, Vendors：显示order_num为20007的物品的prod_name, vend_name, prod_price, quantity
预期结果
+---------------------+-----------------+------------+----------+
| prod_name           | vend_name       | prod_price | quantity |
+---------------------+-----------------+------------+----------+
| 18 inch teddy bear  | Bears R Us      |      11.99 |       50 |
| Fish bean bag toy   | Doll House Inc. |       3.49 |      100 |
| Bird bean bag toy   | Doll House Inc. |       3.49 |      100 |
| Rabbit bean bag toy | Doll House Inc. |       3.49 |      100 |
| Raggedy Ann         | Doll House Inc. |       4.99 |       50 |
+---------------------+-----------------+------------+----------+


''',  
'''
SELECT prod_name, vend_name, prod_price, quantity
FROM OrderItems, Products, Vendors
WHERE Products.vend_id = Vendors.vend_id
 AND OrderItems.prod_id = Products.prod_id
 AND order_num = 20007;
'''),     
     
    ('''假设Customers表中没有重复的姓名，给定一个姓名，比如'Jim Jones'，请找出'Jim Jones'所在公司的所有雇员。
预期结果
+------------+-----------+--------------------+
| cust_id    | cust_name | cust_contact       |
+------------+-----------+--------------------+
| 1000000003 | Fun4All   | Jim Jones          |
| 1000000004 | Fun4All   | Denise L. Stephens |
+------------+-----------+--------------------+
''',  
'''
SELECT c1.cust_id, c1.cust_name, c1.cust_contact
FROM Customers AS c1, Customers AS c2
WHERE c1.cust_name = c2.cust_name
AND c2.cust_contact = 'Jim Jones';
'''),         
     
    ('''
基于Customers和Orders表：  
检索所有顾客(cust_id)及其订单数(order_num为订单号):包括那些至今尚未下订单的顾客;

预期结果
    
+------------+---------+
| cust_id    | num_ord |
+------------+---------+
| 1000000001 |       2 |
| 1000000002 |       0 |
| 1000000003 |       1 |
| 1000000004 |       1 |
| 1000000005 |       1 |
+------------+---------+


''',  
'''
SELECT Customers.cust_id,
COUNT(Orders.order_num) AS num_ord
FROM Customers LEFT OUTER JOIN Orders
ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id;
'''),         
                
            
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
    
ceshidians = ["支付宝APP安卓端安全测试", "ubuntu 20.04安装mysql",
              "ubuntu 20.04使用cp拷贝目录", "钉钉弱网测试"]

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
答题时间50分钟。考试不能代表全部，如果您有其他方面的特长，请在后续面试充分展现自己，谢谢！ 
联系人 钉钉或微信 pythontesting 

1,SQL基础题


'''

dbs = '''

数据库参考（只需关注题目中提及的表即可）：

mysql> select * from Customers;
+------------+---------------+----------------------+-----------+------------+----------+--------------+--------------------+-----------------------+
| cust_id    | cust_name     | cust_address         | cust_city | cust_state | cust_zip | cust_country | cust_contact       | cust_email            |
+------------+---------------+----------------------+-----------+------------+----------+--------------+--------------------+-----------------------+
| 1000000001 | Village Toys  | 200 Maple Lane       | Detroit   | MI         | 44444    | USA          | John Smith         | sales@villagetoys.com |
| 1000000002 | Kids Place    | 333 South Lake Drive | Columbus  | OH         | 43333    | USA          | Michelle Green     | NULL                  |
| 1000000003 | Fun4All       | 1 Sunny Place        | Muncie    | IN         | 42222    | USA          | Jim Jones          | jjones@fun4all.com    |
| 1000000004 | Fun4All       | 829 Riverside Drive  | Phoenix   | AZ         | 88888    | USA          | Denise L. Stephens | dstephens@fun4all.com |
| 1000000005 | The Toy Store | 4545 53rd Street     | Chicago   | IL         | 54545    | USA          | Kim Howard         | NULL                  |
+------------+---------------+----------------------+-----------+------------+----------+--------------+--------------------+-----------------------+

mysql> select * from OrderItems;
+-----------+------------+---------+----------+------------+
| order_num | order_item | prod_id | quantity | item_price |
+-----------+------------+---------+----------+------------+
|     20005 |          1 | BR01    |      100 |       5.49 |
|     20005 |          2 | BR03    |      100 |      10.99 |
|     20006 |          1 | BR01    |       20 |       5.99 |
|     20006 |          2 | BR02    |       10 |       8.99 |
|     20006 |          3 | BR03    |       10 |      11.99 |
|     20007 |          1 | BR03    |       50 |      11.49 |
|     20007 |          2 | BNBG01  |      100 |       2.99 |
|     20007 |          3 | BNBG02  |      100 |       2.99 |
|     20007 |          4 | BNBG03  |      100 |       2.99 |
|     20007 |          5 | RGAN01  |       50 |       4.49 |
|     20008 |          1 | RGAN01  |        5 |       4.99 |
|     20008 |          2 | BR03    |        5 |      11.99 |
|     20008 |          3 | BNBG01  |       10 |       3.49 |
|     20008 |          4 | BNBG02  |       10 |       3.49 |
|     20008 |          5 | BNBG03  |       10 |       3.49 |
|     20009 |          1 | BNBG01  |      250 |       2.49 |
|     20009 |          2 | BNBG02  |      250 |       2.49 |
|     20009 |          3 | BNBG03  |      250 |       2.49 |
+-----------+------------+---------+----------+------------+

mysql> select * from Orders;
+-----------+---------------------+------------+
| order_num | order_date          | cust_id    |
+-----------+---------------------+------------+
|     20005 | 2012-05-01 00:00:00 | 1000000001 |
|     20006 | 2012-01-12 00:00:00 | 1000000003 |
|     20007 | 2012-01-30 00:00:00 | 1000000004 |
|     20008 | 2012-02-03 00:00:00 | 1000000005 |
|     20009 | 2012-02-08 00:00:00 | 1000000001 |
+-----------+---------------------+------------+

mysql> select * from Products;
+---------+---------+---------------------+------------+-----------------------------------------------------------------------+
| prod_id | vend_id | prod_name           | prod_price | prod_desc                                                             |
+---------+---------+---------------------+------------+-----------------------------------------------------------------------+
| BNBG01  | DLL01   | Fish bean bag toy   |       3.49 | Fish bean bag toy, complete with bean bag worms with which to feed it |
| BNBG02  | DLL01   | Bird bean bag toy   |       3.49 | Bird bean bag toy, eggs are not included                              |
| BNBG03  | DLL01   | Rabbit bean bag toy |       3.49 | Rabbit bean bag toy, comes with bean bag carrots                      |
| BR01    | BRS01   | 8 inch teddy bear   |       5.99 | 8 inch teddy bear, comes with cap and jacket                          |
| BR02    | BRS01   | 12 inch teddy bear  |       8.99 | 12 inch teddy bear, comes with cap and jacket                         |
| BR03    | BRS01   | 18 inch teddy bear  |      11.99 | 18 inch teddy bear, comes with cap and jacket                         |
| RGAN01  | DLL01   | Raggedy Ann         |       4.99 | 18 inch Raggedy Ann doll                                              |
| RYL01   | FNG01   | King doll           |       9.49 | 12 inch king doll with royal garments and crown                       |
| RYL02   | FNG01   | Queen doll          |       9.49 | 12 inch queen doll with royal garments and crown                      |
+---------+---------+---------------------+------------+-----------------------------------------------------------------------+

mysql> select * from Vendors;
+---------+-----------------+-----------------+------------+------------+----------+--------------+
| vend_id | vend_name       | vend_address    | vend_city  | vend_state | vend_zip | vend_country |
+---------+-----------------+-----------------+------------+------------+----------+--------------+
| BRE02   | Bear Emporium   | 500 Park Street | Anytown    | OH         | 44333    | USA          |
| BRS01   | Bears R Us      | 123 Main Street | Bear Town  | MI         | 44444    | USA          |
| DLL01   | Doll House Inc. | 555 High Street | Dollsville | CA         | 99999    | USA          |
| FNG01   | Fun and Games   | 42 Galaxy Road  | London     | NULL       | N16 6PS  | England      |
| FRB01   | Furball Inc.    | 1000 5th Avenue | New York   | NY         | 11111    | USA          |
| JTS01   | Jouets et ours  | 1 Rue Amusement | Paris      | NULL       | 45678    | France       |
+---------+-----------------+-----------------+------------+------------+----------+--------------+

'''
print(description)
f.write(description)
shiti = selects[random.randint(1,len(selects)-1)]
print(shiti[0])
f.write(shiti[0] + '\n')
print('\n')
print(shiti[1])
print(dbs)
f.write(dbs)
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
