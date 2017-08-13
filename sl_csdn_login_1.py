#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys  
import requests

reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'  

r = requests.get('http://www.baidu.com')
print r.text
