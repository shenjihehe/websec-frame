import requests
import re
import time
from urllib.parse import urlparse
from lib.core import common
from bs4 import BeautifulSoup
#
#
# def _get_static_post_attr(page_content):
#     """
#     Get params from <input type='hidden'>
#
#     :param page_content:html-content
#     :return dict contains "hidden" parameters in <form>
#     """
#     _dict = {}
#     soup = BeautifulSoup(page_content, "html.parser")
#     for each in soup.find_all('input'):
#
#         if 'value' in each.attrs and 'name' in each.attrs:
#             _dict[each.attrs['name']] = each.attrs['value']
#     print(_dict)
#
#     # _dict["__token__"] = common.GetMiddleStr(page_content,'<input type="hidden" name="__token__" value="','" /></form>')
#
#     return _dict
#
# url = urlparse('http://www.sunbridgegroup.com').netloc
#
# dest = 'http://ce.cloud.360.cn/'
#
# s = requests.session()
#
# data1 = _get_static_post_attr(s.get(dest).content)

url = 'http://ce.cloud.360.cn/'
url = urlparse(url).netloc
print(url)

