#coding:utf-8
import re,urllib2,urllib
def get_content(url):
    """doc"""
    html = urllib2.urlopen(url)
    content = html.read()
    html.close()
    return content
info = get_content('http://tieba.baidu.com/p/2772656630')
def get_pic(info):
    """achive pics"""
    regex = r'class="BDE_Image" src="(.+?\.jpg)"'
    pat = re.compile(regex)
    images_mark = re.findall(pat,info)
    print images_mark
    i = 0
    for image_url in images_mark:
        print image_url
        urllib.urlretrieve(image_url,'%s.jpg' % i)
        i += 1
print get_pic(info)

