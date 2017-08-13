import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    res = urllib2.urlopen(req)
    print res.read()
except urllib2.HTTPError, e:
    print e.code
    print e.reason