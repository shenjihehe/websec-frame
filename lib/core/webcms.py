import json,os,sys,hashlib,threading,queue
from lib.core import Download
from lib.core import outputer


class webcms(object):
    workQueue = queue.Queue()
    URL = ""
    threadNum = 0
    NotFound = True
    Downloader = Download.Downloader()
    result = ""

    def __init__(self,url,threadNum = 10):
        self.URL = url
        self.threadNum = threadNum
        filename = os.path.join(sys.path[0], "data", "data.json")
        fp = open(filename,'r',encoding='utf-8-sig')
        data = json.load(fp)

        for i in data['cms']:
            self.workQueue.put(i)
        fp.close()

    def getmd5(self, body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()

    def th_whatweb(self):
        if(self.workQueue.empty()):
            self.NotFound = False
            return False

        if(self.NotFound is False):
            return False
        cms = self.workQueue.get()
        print(cms)
        print(self.workQueue.get())
        print(self.URL)
        _url = self.URL + cms["url"]
        print(_url)
        html = self.Downloader.get(_url)
        print ("[whatweb log]:checking %s"%_url)
        if(html is None):
            return False
        if cms["re"]:
            if(html.find(cms["re"])!=-1):
                self.result = cms["name"]
                self.NotFound = False
                return True
        else:
            md5 = self.getmd5(html.encode(encoding='gb18030'))
            if(md5==cms["md5"]):
                self.result = cms["name"]
                self.NotFound = False
                return True

    def run(self):
        while(self.NotFound):
            th = []
            for i in range(self.threadNum):
                t = threading.Thread(target=self.th_whatweb)
                t.start()
                th.append(t)
            for t in th:
                t.join()
        if(self.result):
            print ("[webcms]:%s cms is %s"%(self.URL,self.result))
            output.add_list("WebCms识别结果:%s"%self.result)

        else:
            print ("[webcms]:%s cms NOTFound!"%self.URL)
            output.add_list("WebCms识别结果","None" )