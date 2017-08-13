import urllib  
import urllib2  
 
url = 'http://www.xxxxx.com/Portal/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'xxxxx',  'password' : '123456' }  
headers = { 'User-Agent' : user_agent,'Referer':'http://www.xxxxx.com/Portal/' }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read()
print page