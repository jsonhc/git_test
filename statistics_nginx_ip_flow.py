#!/usr/bin/python
#coding=utf8

log_file = "/usr/local/nginx/logs/access.log"

with open(log_file) as f:
    contexts = f.readlines()

# define ip dict###
ip = {}
flow = {}
sum = 0

for line in contexts:
    # count row size of flow
    size = line.split()[9]
    # print ip
    ip_attr = line.split()[0]
    # count total size of flow
    sum = int(size) + sum
    if ip_attr in ip.keys():   # if ip repeated
	# count of ip plus 1
        ip[ip_attr] = ip[ip_attr] + 1
	# size of flow plus size
        flow[ip_attr] = flow[ip_attr] + int(size)
    else:
	# if ip not repeated 
	# define initial values of count of ip and size of flow
        ip[ip_attr] = 1
        flow[ip_attr] = int(size)

print(ip)
print(flow)
print(sum/1024/1024) 
