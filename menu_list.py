作业三：多级菜单
三级菜单
可依次选择进入各子菜单
所需新知识点：列表、字典

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:jsonhc


d = {
    'hubei':{
        'wuhan':['xinzhou','wuchang','hankou']
    },
    'hunan':{
        'changsha':['chengqu','jiaoqu']
    },
    'beijing':['changpingqu','dongchengqu','haidianqu']
}

'''
print(type(d))
for i in d.values():
    for j in i.values():
        print(j)
'''

flag = True
while flag:
    for first in d:    #打印第一级菜单
        print(first)

    choice = input("what is your choice:")  #第一级菜单选择

    if choice in d.keys():  # 当选择属于一级菜单中，打印二级菜单，否则退出
        for list_one in d[choice]:
            print(list_one)
    else:
        break        #一级菜单退出,结束整个菜单循环

    while flag:
        choice2 = input("what is your choice2:")   #第二级菜单选择

        if choice2 == 'b' or choice2 == 'q':     #选择b or q，返回到一级菜单
            break
        else:
            if  type(d[choice]) is dict:     #打印三级菜单
                for i in d[choice][choice2]:
                    print(i)
            else:
                break   #返回到一级菜单

        while flag:
            choice3 = input("please choice3:")        #第三级菜单选择

            if choice3 == 'b':     #返回上一级菜单
                for list_one in d[choice]:    #打印二级菜单
                    print(list_one)
                break
            elif choice3 in d.keys():      #一级菜单选择，并打印二级菜单
                for list_one in d[choice3]:
                    print(list_one)
                break
            else:
                for first in d:  # 打印第一级菜单
                    print(first)






































