#coding:utf-8
import urllib2
#创建密码管理者
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#添加用户名和密码
top_level_url = "http://www.baidu.com"
password_mgr.add_password(None,top_level_url,'992975991@qq.com','15984794312')
#创建一个新的handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
#创建opener
opener = urllib2.build_opener(handler)
a_url = "http://www.baidu.com"
#使用opener获取一个url
opener.open(a_url)
print urllib2.install_opener(opener)
