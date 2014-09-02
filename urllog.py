#1author:luoguoling
import urllib2
httpHandler = urllib2.HTTPSHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
try:
    response = urllib2.urlopen('http://www.google.com',timeout=10)
except:
    print "time is out"
#print response.read()
    print response.getcode()
