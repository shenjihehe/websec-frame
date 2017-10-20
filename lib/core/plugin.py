
import os
import sys
class spiderplus(object):
    # 将插件目录加入到环境变量sys.path
    def __init__(self,plugin,disallow=[]):
        self.dir_exploit = []
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.getcwd()[:-4]+'\\' +plugin
        sys.path.append(plugin)
        sys.path.append(self.plugin)

    # 获取插件，通过对.py的文件扫描得到
    def list_plusg(self):
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True
        dir_exploit = filter(filter_func, os.listdir(self.plugin))
        return list(dir_exploit)

    def work(self,url,html):
        for _plugin in self.list_plusg():

            try:
                m = __import__(_plugin.split('.')[0]) #动态调用
                spider = getattr(m, 'spider')
                p = spider()
                s =p.run(url,html)
            except Exception as e:
                print(e)