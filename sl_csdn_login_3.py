#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
# 使用beautifulsoup来处理获取的html内容，这个库需要安装，还是使用pip install beautifulsoup4来安装
from bs4 import BeautifulSoup as bs

reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'  
# 这个函数使用来提取流水号的
def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''
    soup = bs(str)
    tt = {}
    # 提取form表单中所有的input标签，以字典的形式来保存name：value
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            tt[inp.get('name')] =inp.get('value')
    return tt
    
# 这行代码，是用来维持cookie的，你后续的操作都不用担心cookie，他会自动带上相应的cookie
s = requests.Session()
#header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
r = s.get("http://passport.csdn.net/account/login")
soup = toJson(r.text)
# 我们需要带表单的参数,这里面有个参数lt,登录操作的流水号，我们需要从html页面中进行提取
#payload ={'username':'xxxx','password':'xxxx','lt':soup["lt"],'execution':'e1s1','_eventId':'submit'}
#r = s.post("http://passport.csdn.net/account/login",data=payload,headers=header)
#print r.text
print soup["lt"]