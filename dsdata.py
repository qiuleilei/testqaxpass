#! /usr/bin/python
# coding:utf-8

import urllib2
import sys,os
import re
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
reload(sys)
sys.setdefaultencoding('utf-8')

def chuzi(number):

    headers = {'Content-Type': 'application/json; charset=UTF-8',
           'Authorization': 'MjcxMzU1ODYwMDA2MzY4NTc2NDoyNzc2Nzk2NzU0OTI5MDMwMTgyOjRhNmMwZjM1LWQxMTgtNDcwYi1iMjcyLWI1NGIwMDBkNWM2Ng==',
           'Referer': 'https://10.51.28.130:30443/dsmas/system/assets-manage',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
          }

    url = 'https://10.51.28.130:30443/dayu/v1/dssa/adsg/api/asset/list?content=&pageNumber=%s&pageSize=1000'% number

    rep = requests.get(url,verify=False,headers=headers)
    alist = []
    sec_results =  rep.json()
    results = sec_results['data']
    list_results = results['list']
    for line in list_results:
        if line['port'] != 22:
            alist.append(line['id'])
    print alist

    url2 = 'https://10.51.28.130:30443/dayu/v1/dssa/adsg/api/asset/ignore'

    datas_ids= ",".join(str(i) for i in alist)
    yids = {"ids":''}
    yids['ids']=datas_ids
    yids=json.dumps(yids)

    rep = requests.put(url2,verify=False,headers=headers, data=yids)
    sec_s = rep.json()
    print sec_s
    if sec_s['code'] == 0:
        flasts = 1
    else:
        flasts = 0

    return flasts


if __name__ == "__main__":
    flasts = 1
    i = 1
    while flasts== 1:
        flasts = chuzi(i)
        i= i+1

