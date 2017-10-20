#-*- coding:utf-8 -*-

from lib.core import Download,common
import sys,os
from lib.core import outputer
from lib import websec

payload = []
filename = os.path.join(sys.path[0],"data","xss.txt")
f = open(filename,'r',encoding='ISO-8859-1')
for i in f:
    payload.append(i.strip())

class spider():
    def run(self,url,html):
        download = Download.Downloader()
        urls = common.urlsplit(url)

        if urls is None:
            return False
        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace("my_Payload",_payload)
                print ("[xss test]:",_url)
                #对URL每个参数进行拆分,测试
                _str = download.get(_url)
                if _str is None:
                    return False
                if(_str.find(_payload)!=-1):
                    print ("xss found:%s"%url)
                    websec.output.add_list("Xss", "url:%s payload:%s"%(url,_url))
        return False