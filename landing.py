#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:jsonhc

#f = open(r'D:\study\project\day1\file_new.txt','w')
#f.write("hello world")

'''
作业需求：

① 输入用户名密码

② 认证成功后显示欢迎信息

③ 输错三次后锁定
'''

'''
>>> i = "hello world"
>>> i.strip()
'hello world'
>>> i = "hello world    "
>>> i.strip()     #strip()方法去掉末尾空格字符
'hello world'
>>> i.strip().split()   #split()方法：以空格为切割符切割字符串
['hello', 'world']
>>> i = "hello,world"
>>> i.split(',')
['hello', 'world']
'''

#初始化用户列表，和所用户，将用户和密码保存到用户字典中，锁定用户保存到锁列表中
user_list = {}
lock_user = []

'''
f2 = open(r'D:\study\project\day1\lock.txt','r')
for i in f2.readlines():
    user = i.strip()
    print(user)
    lock_user.append(user)
    print(lock_user)

if 'huang' in lock_user:
    print("OK")
f2.close()
'''

#将用户的账号密码保存在字典中
with open(r'D:\study\project\day1\user.txt','r') as f1:
    for i in f1.readlines():
        (user,password) = i.strip().split()
        user_list[user] = password


#将锁用户的用户报错在一个list中
with open(r'D:\study\project\day1\lock.txt','r') as f2:
    for i in f2.readlines():
        user = i.strip()
        lock_user.append(user)



#用户注册
def user_register():
  username = input("username:")
  password = input("password:")

  with open(r'D:\study\project\day1\user.txt','r+') as f4:
      user_list[username] = password
      for k,v in user_list.items():
          f4.write("%s  %s\n" % (k,v))
  print("Welcome to register!")

count = 0


while count < 3:
    username = input("username:")
    password = input("password:")
    #检测输入的用户是否存在锁用户的list中
    if username in lock_user:
        print("the user is locked,please exit！")
        break

    else:
        #用户存在用户list中，进行密码判断
        if username in user_list.keys():
            if password == user_list[username]:
                print("Welcome to landing!")
                break
            else:
                #密码错误，进行循环输入，超过三次将被锁定
                print("username or password is wrong!")
                count += 1
                continue
        else:
            #用户不存在用户list中，请注册！
            print("username is not exist,please register!")
            user_register()
            break


else:
    print("you have tried too many times,the username will be locked!")
    lock_user.append(username)
    with open(r'D:\study\project\day1\lock.txt','r+') as f3:  #r+可以以追加的方式写入
        for i in lock_user:
            f3.write('%s\n' % i)

