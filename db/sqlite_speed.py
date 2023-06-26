import random
import time

from num2word import word
import sqlite3


def open_database():
    
    db = 'pydb.db'
    conn = sqlite3.connect(db)
    return conn

def get_conn_and_cursor(name, sql=''):
    
    print("*"*20, name)
    conn = open_database()
    cursor = conn.cursor()
    if sql:
        cursor.execute(sql)
        conn.commit();    
    return conn, cursor

def list2file(lists, filename):
    
    f = open(filename, 'w')
    for item in lists:
        f.write(item + "\n")
    f.close()
    

def insert_1000():
    
    sqls = []
    sql = ''' DROP TABLE IF EXISTS t1;'''
    sqls.append(sql)
    conn, cursor = get_conn_and_cursor("Test 1: 1000 INSERTs", sql)
    
    t1 = time.time()   
    sql = ''' CREATE TABLE t1(a INTEGER, b INTEGER, c VARCHAR(100));'''
    cursor.execute(sql)
    conn.commit()
    for i in range(1, 1001):
        num = random.randint(1, 100000000)
        num_str = word(num).lower()
        sql = '''INSERT INTO t1 VALUES({}, {},'{}');'''.format(i, num, num_str)
        cursor.execute(sql)
        sqls.append(sql)
        conn.commit()    
    print("*"*10, time.time()-t1)
    list2file(sqls, "1.sql")
    conn.close()
    
def insert_25000_transaction():
    
    sqls = []
    sql = '''DROP TABLE IF EXISTS t2;'''
    sqls.append(sql)
    conn, cursor = get_conn_and_cursor("Test 2: 25000 INSERTs in a transaction", sql)
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    sql = ''' CREATE TABLE t2(a INTEGER, b INTEGER, c VARCHAR(100));'''
    sqls.append(sql)
    cursor.execute(sql)
    for i in range(1, 25001):
        num = random.randint(1, 100000000)
        num_str = word(num).lower()
        sql = '''INSERT INTO t2 VALUES({}, {},'{}');'''.format(i, num, num_str)
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit()  
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "2.sql")
    
def insert_25000_transaction_index():
    
    sqls = []
    sql = '''DROP TABLE IF EXISTS t3;'''
    sqls.append(sql)
    conn, cursor = get_conn_and_cursor("Test 3: 25000 INSERTs into an indexed table", sql)    
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    sql = ''' CREATE TABLE t3(a INTEGER, b INTEGER, c VARCHAR(100));'''
    sqls.append(sql)
    cursor.execute(sql)
    sql = '''CREATE INDEX i3 ON t3(c);'''
    sqls.append(sql)
    cursor.execute(sql)    
    for i in range(1, 25001):
        num = random.randint(1, 100000000)
        num_str = word(num).lower()
        sql = '''INSERT INTO t1 VALUES({}, {},'{}');'''.format(i, num, num_str)
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit()  
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "3.sql")
    
    
def select_100_without_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 4: 100 SELECTs without an index")        
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    for i in range(100):
        sql = '''SELECT count(*), avg(b) FROM t2 WHERE b>={} AND b<{};'''.format(i*100, i*100+1000)
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit() 
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "4.sql")
    

def select_100_comparison():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 5: 100 SELECTs on a string comparison")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    for i in range(1,101):
        sql = '''SELECT count(*), avg(b) FROM t2 WHERE c LIKE '%{}%';'''.format(word(i).lower())
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit() 
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "5.sql")
    
def create_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 6: Creating an index")
 
    t1 = time.time()   
    sql = ''' CREATE INDEX i2a ON t2(a);'''
    sqls.append(sql)
    cursor.execute(sql)   
    conn.commit() 
    sql = ''' CREATE INDEX i2b ON t2(b); '''
    sqls.append(sql)
    cursor.execute(sql)   
    conn.commit() 
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "6.sql")
    
def select_5000_with_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 7: 5000 SELECTs with an index")
 
    t1 = time.time()   
    for i in range(5000):
        sql = '''SELECT count(*), avg(b) FROM t2 WHERE b>={} AND b<{};'''.format(i*100, i*100+100)
        sqls.append(sql)
        cursor.execute(sql)
        conn.commit()    
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "7.sql")


def update_1000_without_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 8: 1000 UPDATEs without an index")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    for i in range(1000):
        sql = '''UPDATE t1 SET b=b*2 WHERE a>={} AND a<{};'''.format(i*10, i*10+10)
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit()   
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "8.sql")
    
def update_25000_with_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 9: 25000 UPDATEs with an index")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    for i in range(25000):
        sql = '''UPDATE t2 SET b={} WHERE a={};'''.format(random.randint(1, 100000000), i+1)
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit()   
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "9.sql")
    
def update_25000_text_with_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 10: 25000 text UPDATEs with an index")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    for i in range(25000):
        sql = '''UPDATE t2 SET c='{}' WHERE a={};'''.format(word(random.randint(1, 100000000)).lower(), i+1)
        cursor.execute(sql)
        sqls.append(sql)
    conn.commit()  
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "10.sql")

def insert_from_select():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 11: INSERTs from a SELECT")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    sql = '''INSERT INTO t1 SELECT b,a,c FROM t2;'''
    sqls.append(sql)
    cursor.execute(sql)
    sql = '''INSERT INTO t2 SELECT b,a,c FROM t1;'''
    sqls.append(sql)
    cursor.execute(sql)  
    conn.commit() 
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "11.sql")
    

def del_without_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 12: DELETE without an index")
 
    t1 = time.time()   
    sql = '''DELETE FROM t2 WHERE c LIKE '%fifty%'; '''
    sqls.append(sql)
    cursor.execute(sql)  
    conn.commit() 
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "12.sql")
    
def del_with_index():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 13: DELETE with an index")
 
    t1 = time.time()   
    sql = '''DELETE FROM t2 WHERE a>10 AND a<20000;  '''
    sqls.append(sql)
    cursor.execute(sql)  
    conn.commit() 
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "13.sql")
    
def big_insert_after_big_del():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 14: A big INSERT after a big DELETE")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    sql = '''DELETE FROM t2;'''
    sqls.append(sql)
    cursor.execute(sql)
    sql = '''INSERT INTO t2 SELECT * FROM t1; '''
    sqls.append(sql)
    cursor.execute(sql)  
    conn.commit()
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "14.sql")


def small_insert_after_big_del():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 15: A big DELETE followed by many small INSERTs")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    sql = '''DELETE FROM t1;'''
    sqls.append(sql)
    cursor.execute(sql)
    for i in range(1, 12001):
        num = random.randint(1, 100000000)
        num_str = word(num).lower()
        sql = '''INSERT INTO t1 VALUES({}, {},'{}');'''.format(i, num, num_str)
        sqls.append(sql)
        cursor.execute(sql)
    conn.commit() 
    sqls.append("COMMIT;")
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "15.sql")
    
def drop_table():
    
    sqls = []
    conn, cursor = get_conn_and_cursor("Test 16: DROP TABLE")
 
    t1 = time.time()   
    cursor.execute("BEGIN")
    sqls.append("BEGIN;")
    sql = '''DROP TABLE t1;'''
    sqls.append(sql)
    cursor.execute(sql)
    conn.commit() 
    sql = '''DROP TABLE t2;'''
    sqls.append(sql)
    cursor.execute(sql)
    conn.commit() 
    sql = '''DROP TABLE t3;'''
    sqls.append(sql)
    cursor.execute(sql)
    conn.commit() 
    print("*"*10, time.time()-t1)
    conn.close()
    list2file(sqls, "16.sql")
    
insert_1000()
insert_25000_transaction()
insert_25000_transaction_index()
select_100_without_index()
select_100_comparison()
create_index()
select_5000_with_index()
update_1000_without_index()
update_25000_with_index()
update_25000_text_with_index()
insert_from_select()
del_without_index()
del_with_index()
big_insert_after_big_del()
small_insert_after_big_del()
drop_table()

