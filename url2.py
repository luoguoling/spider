from urllib2 import Request,urlopen,URLError,HTTPError
def url2():
    url = "http://www.baidu.com/"
    req = Request(url)
    try:
        response = urlopen(req)
        print response.read()
        print response.geturl()
        print response.getcode()
    except URLError,e:
        if hasattr(e,'code'):
            print 'the server can not achiee'
            print 'Error code',e.code
        elif hasattr(e,'reason'):
            print 'Error reason',e.reason
        else:
            print 'no exception'
    
url2()
