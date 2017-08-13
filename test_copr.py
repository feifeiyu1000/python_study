#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import requests

reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'  

s = requests.Session()
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0','X-DevTools-Emulate-Network-Conditions-Client-Id':'f7c50f47-333e-4c31-b304-050acb7f0570'}
payload ={'txtUsername':'zhudongyang','txtPassword':'lr1202','__EVENTTARGET':'ResourceManager1','__EVENTARGUMENT':'B_Login|event|Click'}
r = s.post("http://checkin.longruan.com/V2/HBBX/Default.aspx",data=payload,headers=header)
#print r.text
print r.text