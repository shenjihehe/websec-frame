import json
import sys,os
import demjson



fq = open("data.json",'r',encoding='utf-8')
data =json.load(fq)
list = []
url_list=[]
for i in  data['cms']:
    list.append(i)

    if i['url'] not in url_list:
        url_list.append(i['url'])

fq.close()

f =open("data.txt",'r',encoding='utf-8')
for i in f.readlines():
    i=i.split('|')
    i[2] = i[2].strip()
    if i[1] not in url_list:
        info = {
                        "url":i[0],
                        "re":"",
                        "name":i[1],
                        "md5":i[2]
                    }
        list.append(info)

wb_data = {'cms':list}





fq = open("data.json",'w',encoding='utf-8')
fq.write(json.dumps(wb_data, sort_keys=True, indent=4, separators=(',', ': ')))
fq.close()






