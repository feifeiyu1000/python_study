#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
#headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'username':'zhuzhudong1@163.com',
			'password':'QAZXCV'
		})
#登录教务系统的URL
#loginUrl = 'http://www.gzaqy.com/cas/login?service=http://www.gzaqy.com/Base/'
#loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
req = urllib2.Request(url = 'https://passport.csdn.net/account/login',headers = hdr)
#loginUrl = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
#模拟登录，并把cookie保存到变量
pdb.set_trace() 
pdb.set_trace() 
result = opener.open(req,postdata)
#result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
#gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#gradeUrl = 'http://www.gzaqy.com/Base/home/enterprise#sys/Safety/index/index'
gradeUrl = 'http://my.csdn.net/my/mycsdn'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()