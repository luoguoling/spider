#author:luoguoling
import urllib,string
def get_bdtieba(bdurl,beginpage,endpage):
    """
    @bdurl:source url
    @beginpage:the begin page
    @endpage:the end page
    """
    for i in range(beginpage,endpage):
        sName = string.zfill(i,5) + '.html'
        print 'doloading' + str(i) + 'page'
        f = open(sName,'w+')
        m = urllib.urlopen(bdurl + str(i)).read()
        f.write(m)
        f.close()
bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
beginpage=1
endpage=10
get_bdtieba(bdurl,beginpage,endpage)
