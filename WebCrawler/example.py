#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

class CSDN(object):
    def __init__(self, headers):
        self.session = requests.Session()
        self.headers = headers
    def get_webflow(self):
        url = 'http://passport.csdn.net/account/login'
        response = self.session.get(url=url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        lt = soup.find('input', {'name': 'lt'})['value']
        execution = soup.find('input', {'name': 'execution'})['value']
        soup.clear()
        return (lt, execution)
    def login(self, account, password):
        self.username = account
        self.password = password
        lt, execution = self.get_webflow()
        data = {
            'username': account,
            'password': password,
            'lt': lt,
            'execution': execution,
            '_eventId': 'submit'
        }
        url = 'http://passport.csdn.net/account/login'
        response = self.session.post(url=url, headers=self.headers, data=data)
        if (response.status_code == 200):
            print('正常')
        else:
            print('异常')
    def func(self):
        headers1={
            'Host':'write.blog.csdn.net',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }
        response=self.session.get(url='http://write.blog.csdn.net/postlist',headers=headers1,allow_redirects=False)
        print response.text
if __name__ == '__main__':
    headers = {
        'Host': 'passport.csdn.net',
        'Origin': 'http://passport.csdn.net',
        'Referer':'http://passport.csdn.net/account/login',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    }
    csdn = CSDN(headers=headers)
    account = ''
    password = ''
    csdn.login(account=account, password=password)
    csdn.func()