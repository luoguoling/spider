#!/usr/bin/python
#author:luoguoling
import re,urllib2,MySQLdb
from BeautifulSoup import BeautifulSoup
aaa = 3000
url1 = "http://bbs.ustc.edu.cn/cgi/bbstdoc?board=PieBridge&start="
while aaa > 0:
    aaa = aaa - 20
    aaa1 = str(aaa)
    url11 = url1 + aaa1
    fp = urllib2.urlopen(url11)
    try:
        p = fp.read().decode("gb2312",'ignore')
        p = re.sub("charset=gb2312","charset=utf-8",p,re.I)
        p = p.encode('utf-8','ignore')
    except:
        p = fp.read()
    soup = BeautifulSoup(p)
    polist = soup.findAll('span')
    print polist[2].contents[1]

def connect(sql):
    db = MySQLdb.connect(host="localhost",user="root",passwd="abc123?",db="spider",use_unicode=1,charset="utf-8")
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

