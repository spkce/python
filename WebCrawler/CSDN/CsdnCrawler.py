#encoding:utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

url_login = 'https://passport.csdn.net/account/verify'
url = "http://blog.csdn.net"
cookie = cookielib.MozillaCookieJar('cppkies.txt')
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)


headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
headers['Referer'] = 'https://passport.csdn.net/account/login'

value = {}
value['username'] = 'm15188159686@163.com'
value['password'] = 'Ajk12345yu'
value['lt'] = 'LT-129493-lYxOUdgttXK3p6SoFZWg94ZPAZU6CW'
value['execution'] = 'e5s1'
value['_eventId'] = 'submit'

data = urllib.urlencode(value) 

opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36")]
#request = urllib2.Request(url_login, data=data, headers)

#登陆前准备：获取lt和exection
response = opener.open(url_login)
soup = BeautifulSoup(response.read(),"html5lib")
for input in  soup.form.find_all("input"):
    if input.get("name") == "lt":
        value['lt'] = input.get("value")
        print value['lt']
    if input.get("name") == "execution":
        value['execution'] = input.get("value")
        print value['execution']
 
 
response = opener.open(url_login, data=data)

cookie.save(ignore_discard=True, ignore_expires=True)

a={}

for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
    a[item.name] = item.value

data = urllib.urlencode(a) 

print data

#opener.addheaders[("Cookie",data)]
request = urllib2.Request('http://msg.csdn.net/letters')
response = opener.open(request)

f = open('csdn_index.html', 'w')
f.write(response.read());
f.close()
