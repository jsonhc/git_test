#!/usr/bin/python
#coding=utf8

import cx_Oracle as oracle

db = oracle.connect('scott/redhat@192.168.223.138:1521/oracle.test')

cursor = db.cursor()

cursor.execute('select sysdate from dual')

data = cursor.fetchone()

print('Database time:%s' % data)

cursor.close()
db.close()
