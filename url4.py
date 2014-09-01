#coding:utf-8
import random
import urllib2
url = "http://blog.csdn.net/yuanmeng001"
my_headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
        'Host':'blog.csdn.net',
        'Referer':'http://blog.csdn.net',
        'GET':url
        }
headers = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'
        ]
def getContent(url,headers):
    """
    @achiveve403webpage
    """
    random_values = random.choice(headers)
    print random_values
    req = urllib2.Request(url)
    req.add_header('User-Agent',random_values)
    req.add_header('Host','blog.csdn.net')
    req.add_header('Referer','http://blog.csdn.net')
    req.add_header('GET',url)
    content = urllib2.urlopen(req).read()
    
    return content,random_values

html = getContent(url,headers)
print html
#a = urllib2.Request(url,headers=my_headers)
#html = urllib2.urlopen(a)
#print html.read()
#print a.headers.items()
