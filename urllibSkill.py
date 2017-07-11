# _*_ coding: utf-8 _*_
# _*_ Python 2.7.10 _*_
# _*_ urllib库的基本使用 _*_

import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()

#url一般接受三个参数
#urlopen(url, data, timeout)

#POST方式
import urllib

values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

#GET方式
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

