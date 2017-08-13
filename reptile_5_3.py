import urllib2

req = urllib2.Request('http://xxxx.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print "first"
    print e.code
except urllib2.URLError, e:
    print e.reason
    print "first"
else:
    print "OK"