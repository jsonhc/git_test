#!/usr/bin/python
#coding=utf8

log_file = "/usr/local/nginx/logs/access.log"

with open(log_file) as f:
    contexts = f.readlines()

# define ip dict###
ip = {}

for line in contexts:
    #size = line.split()[9]
    # str split
    ip_attr = line.split()[0]
    if ip_attr in ip.keys():
        ip[ip_attr] = ip[ip_attr] + 1
    else:
        ip[ip_attr] = 1

print(ip)
    
