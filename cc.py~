#!/usr/bin/python
import re
dic = {}
file = open('p1.py','r')
for (num,value) in enumerate(file):
    dic[num] = value
for k,v in dic.items():
    if v == 'while aaa > 0:\n':
        print k
        print dic[k-1]
#print x
file.close()
#p1 = re.search('import',p)
#print p1.group(0)
