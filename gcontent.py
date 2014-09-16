#coding:utf-8
import re,urllib,urllib2,thread,time
class Spider_Model:
    """
    """
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
    def GetPage(self,page):
        myUrl = "http://m.qiushibaike.com/hot/page" + page
        user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        headers = {'User-Agent':user_agent}
        req = urllib2.Request(myUrl,headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        unicodePage = myPage.decode("utf-8")
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
        items = []
        for item in myItems:
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])
        return items
        
    def LoadPage(self):
        """
        用于加载
        """
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print 'can not open baike'
            else:
                time.sleep(1)
    def ShowPage(self,nowPage,page):
        for items in nowPage:
            print u'第%d页' % page ,items[0],items[1]
            myInput = raw_input()
            if myInput == "quit":
                self.enable = False
                break
    def Start(self):
        self.enable = True
        page = self.page
        print u'loading....'
        thread.start_new_thread(self.LoadPage,())
        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1
print u"""
    version:1.0
    """
print u'please enter the page'
raw_input('')

Spider = Spider_Model()
Spider.Start()
