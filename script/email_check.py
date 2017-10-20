import re
from lib.core import outputer
from lib import websec

class spider():
    def run(self,url,html):
        #print(html)
        pattern = re.compile(r'([\w-]+@[\w-]+\.[\w-]+)+')
        email_list = re.findall(pattern, html)
        if(email_list):
            print(email_list)
            websec.output.add_list("email", "%s"%email_list)
            return True
        return False