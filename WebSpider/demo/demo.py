#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
#ÍøÖ·
url = "http://www.baidu.com/"
#ÇëÇó
request = urllib.request.Request(url)
#½âÎö
response = urllib.request.urlopen(request)

data = response.read()

#data = data.decode('utf-8')

print(data)

print("2")