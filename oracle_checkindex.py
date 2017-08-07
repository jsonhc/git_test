#!/usr/bin/python
#coding=utf8

import cx_Oracle as oracle
from email_function import send_mail

def oraclesql(cursor):
   fp = open(r'/home/oracle/scripts/checkindex.sql')
   fp_sql = fp.read()
   cursor.execute(fp_sql)
   fp.close()
   data = cursor.fetchall()
   return data


if __name__ == '__main__':
   ipaddr = "192.168.223.138"
   username = "system"
   password = "redhat"
   oracle_port = "1521"
   oracle_service = "oracle.test"
   try:
      db = oracle.connect(username+"/"+password+"@"+ipaddr+":"+oracle_port+"/"+oracle_service)
   except Exception as e:
      print(e)
   else:
      cursor = db.cursor()
      data = oraclesql(cursor)
      cursor.close()
      db.close()
      for i in data:
          print(i)
