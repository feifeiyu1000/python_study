import urllib  
import urllib2  
 
url = 'http://www.gzaqy.com/Portal/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'mlmkadmin',  'password' : '123456' }  
headers = { 'User-Agent' : user_agent,'Referer':'http://www.gzaqy.com/Portal/' }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read()
print page