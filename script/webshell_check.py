import os
import sys
from lib.core import outputer
from lib.core.Download import Downloader
from lib import websec

filename = os.path.join(sys.path[0],"data","web_shell.txt")
payload = []
f = open(filename,'r',encoding='ISO-8859-1')
a = 0
for i in f:
    payload.append(i.strip())
    a+=1
    if(a==999):
        break

class spider:
    def run(self,url,html):
        if(not url.endswith(".php")):
            return False
        print ('[Webshell check]:',url)
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s";' % _payload
            r = Downloader.post(url,post_data)
            if(r):
                print("webshell:%s"%r)
                websec.output.add_list("webshell", "url:%s password:%s"%(url,r))
                return True
        return False