#-*- coding: utf-8 -*-

#尝试用正则过滤UA中的信息

import re

#测试用数据
ua = ['''Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; Tablet PC 2.0; InfoPath.3; CIBA; Maxthon 2.0)''',
'''Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1''',
'''Mozilla/4.0 (compatible; MSIE 5.50; Windows 95; SiteKiosk 4.8)''',
'''Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC)''',
'''Mozilla/2.0 (compatible; MSIE 3.0B; Windows NT)''',
'''Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)''']

IE = re.compile('(?<=MSIE\s)\d+\.\d+')
Windows = re.compile('(?<=Windows\s)[^;)]+')
Chrome = re.compile('(?<=Chrome/)\d+\.\d+')


def test(uaStr):
    m = Windows.search(uaStr)
    if m:
        print('Windows',m.group())
    m = IE.search(uaStr)
    if m:
        print('IE',m.group())
    m = Chrome.search(uaStr)
    if m:
        print('Chrome',m.group())
    print()


for s in ua:
    test(s)

#('Windows', 'NT 6.1')
#('IE', '7.0')
#()
#('Windows', 'NT 5.1')
#('Chrome', '21.0')
#()
#('Windows', '95')
#('IE', '5.50')
#()
#('Windows', 'CE')
#('IE', '4.01')
#()
#('Windows', 'NT')
#('IE', '3.0')
#()
#('Windows', '3.1')
#('IE', '2.0')
#()


