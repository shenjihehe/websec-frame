#-*- coding:utf-8 -*-

import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms, common, PortScan,webdir,CDN_Scan
from lib.core import outputer
from urllib.parse import urlparse

output = outputer.outputer()


def main():
    root = "http://www.sunbridgegroup.com"
    # root = "http://www.china-zmc.com"
    threadNum = 10

    domain = urlparse(root).netloc




    # CDN_Scan
    print("CDN检查中")
    msg,iscdn = CDN_Scan.checkCDN(root)
    print(msg)
    output.add("CDN",msg)
    if iscdn:
        # IP Port Scan
        ip = common.gethostbyname(root)
        print("IP:", ip)
        print("Start Port Scan:")
        pp = PortScan.PortScan(ip)
        pp.work()
        output.build_html(domain)

    # Dir Fuzz
    # dd = webdir.webdir(root,threadNum)
    # dd.work()
    # dd.output()
    # output.build_html(domain)

    #webcms
    # ww = webcms.webcms(root,threadNum)
    # ww.run()
    # output.build_html(domain)

    #spider
    # w8 = SpiderMain(root,threadNum)
    # w8.craw()

if __name__ == '__main__':
    main()