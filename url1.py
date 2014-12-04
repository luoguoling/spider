import urllib
def callback(a,b,c):
    """
    @a:num
    @b:large
    @c:remote file large
    """
    down_progress = 100.0*a*b/c
    if down_progress > 100:
        down_progress = 100
    print "%.2f%%" % down_progress
    print a*b

url = "http://www.python.org"
urllib.urlretrieve(url,"c.html",callback)
html = urllib.urlopen(url)
header = html.info()
print header.getparam('charset')
