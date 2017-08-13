import urllib
import urllib2

values = {}
values['username'] = "xxxx@qq.com"
values['password'] = "xxxx"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl