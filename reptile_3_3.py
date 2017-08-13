import urllib
import urllib2

values = {"username":"zfffeeeii","password":"xxxx","lt":"LT-222045-6laY9fJVWYZdv0eNLQX3mmgP0EReSL","execution":"e4s1","_eventId":"submit"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()