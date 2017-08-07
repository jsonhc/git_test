#!/usr/bin/python
#coding=utf8

import cx_Oracle as oracle
from email_function import send_mail
import sys

def oraclesql(cursor):
   fp = open(r'/home/oracle/scripts/checkindex.sql')
   fp_sql = fp.read()
   cursor.execute(fp_sql)
   fp.close()
   data = cursor.fetchall()
   return data


if __name__ == '__main__':
   username = sys.argv[1]
   password = sys.argv[2]
   tnsname = sys.argv[3]
   try:
      db = oracle.connect(username+"/"+password+"@"+tnsname)
   except Exception as e:
      print(e)
   else:
      cursor = db.cursor()
      data = oraclesql(cursor)
      cursor.close()
      db.close()
      for i in data:
          print(i)
