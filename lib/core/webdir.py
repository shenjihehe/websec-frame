import os
import sys
import queue
import requests
import threading
from lib.core import outputer
from lib import websec

class webdir:
    def __init__(self,root,threadNum):
        self.root = root
        self.threadNum = threadNum
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
             'Referer': 'http://www.baidu.com',
             'Cookie': 'whoami=user',
             }#自行根据情况更改headers头
        self.task = queue.Queue()
        self.s_list = []
        # 加载目录字典
        filename = os.path.join(sys.path[0], "data", "dir.txt")
        for line in open(filename,encoding='utf-8'):
            self.task.put(root + line.strip())

    # 检测网页状态
    def checkdir(self,url):
        status_code = 0
        try:
            # 访问网页头来判断返回的状态码
            r = requests.head(url,headers=self.headers)
            status_code = r.status_code
        except:
            status_code = 0
        return status_code

    # 线程函数
    # 从队列中取出数据再循环访问
    def test_url(self):
        while not self.task.empty():
            url = self.task.get()
            s_code = self.checkdir(url)
            if s_code==200:
                self.s_list.append(url)
                websec.output.add_list("Web敏感目录",url )
            print ("Testing: %s status:%s"%(url,s_code))


    # 启动线程
    def work(self):
        threads = []
        for i in range(self.threadNum):
            t = threading.Thread(target=self.test_url())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('[*] The DirScan is complete!')

    # 输出函数
    def output(self):
        if len(self.s_list):
            print("[*] status = 200 dir:")
            for url in self.s_list:
                print(url)