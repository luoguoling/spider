import chardet,urllib
url = "http://www.163.com"
content = urllib.urlopen(url).read()
print chardet.detect(content)
def automatic_detect(url):
    content = urllib.urlopen(url).read()
    result = chardet.detect(content)
    encoding = result['encoding']
    return encoding
a = automatic_detect(url)
print a
