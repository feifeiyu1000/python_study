#!/usr/local/bin/python
# -*- coding: cp936 -*-ookielib
import urllib2

response = urllib2.urlopen("http://www.05147.net/portal.php")
print response.read ()