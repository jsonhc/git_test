#!/usr/bin/python
#coding=utf8

log_file = "/usr/local/nginx/logs/access.log"

with open(log_file) as f:
  contexts = f.readlines()

url = {}

for line in contexts:
  url_attr  = line.split()[6]
  if url_attr in url.keys():
    url[url_attr] = url[url_attr] + 1
  else:
    url[url_attr] = 1

print(url)
