#encoding:utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup


class CsdnCrawler(object):
    def __init__(self, cookies_save_path):
        self.url_login = 'https://passport.csdn.net/account/verify'
        self.cookie = cookielib.MozillaCookieJar(cookies_save_path)
        self.handler = handler=urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.handler)
    #登陆前准备：获取lt和exection
    def __get_login_param(self):
        lt = ''
        execution = ''
        self.opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36")]
        response = self.opener.open(self.url_login)

        soup = BeautifulSoup(response.read(), 'html.parser')
        lt = soup.find('input', {'name': 'lt'})['value']
        execution = soup.find('input', {'name': 'execution'})['value']
        soup.clear()
        return (lt, execution)
    #login
    def login(self, username, password):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        headers['Referer'] = 'https://passport.csdn.net/account/login'

        lt, execution = self.__get_login_param()
        value = {}
        value['username'] = username
        value['password'] = password
        value['lt'] = lt
        value['execution'] = execution
        value['_eventId'] = 'submit'
    
        data = urllib.urlencode(value)
        response = self.opener.open(self.url_login, data=data)
        self.cookie.save(ignore_discard=True, ignore_expires=True)
    #取得登陆后才可见的网页
    def get_web(self, url):
        request = urllib2.Request(url)
        return self.opener.open(request)
 








