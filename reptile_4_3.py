import urllib2
uri = "http://www.baidu.com"
request = urllib2.Request(uri)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)
print response.read()