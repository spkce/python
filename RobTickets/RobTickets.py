#!/usr/bin/python
import os
import urllib
import urllib2
import Tkinter


top = Tkinter.Tk()

#top.mainloop()




'''
url_Login = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
headers = {}
headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers['Referer'] = 'https://kyfw.12306.cn/otn/login/init'
value = {"answer":"37,48","login_site":"E","rand":"sjrand"}
#data =  urllib.urlencode(value)
data = 'answer=37%2C48&login_site=E&rand=sjrand'
#print data


request = urllib2.Request(url_Login, data=data,headers=headers)

respone = urllib2.urlopen(request)

'''
url_Login ='https://passport.csdn.net/account/verify'
headers = {}
headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers['Referer'] = 'https://kyfw.12306.cn/otn/login/init'
value = {}
value['gps'] = None
value['username'] = 'm15188159686@163.com'
value['password'] = 'jk12345yu'
value['rememberMe'] = 'true'
value['lt'] = 'LT-213464-uQeZhb9UG0R5fWa0Bw6sMWu0WO2MWs'
value['execution'] = 'e3s1'
value['_eventId'] = 'submit'

data =  urllib.urlencode(value)

#print data


request = urllib2.Request(url_Login, data=data,headers=headers)

respone = urllib2.urlopen(request)
#respone.read()
#print respone.read()
f=open('Txt.html','wb')
f.write(respone.read())
f.close()