#!/usr/bin/env python
#  -*- coding:utf-8 -*-

from ftplib import FTP
import datetime
 

class CFtp():
	def __init__(self):
		self.ftp = FTP()

	def connect(self, host, port, username, password):
		self.ftp.connect(host, port, 30)
		self.ftp.login(username, password)

	def download(self, remotepath, localpath):
		self.ftp.cwd(remotepath)  # 设置FTP远程目录(路径)
		list = self.ftp.nlst()  # 获取目录下的文件,获得目录列表

		for name in list:
			print(name)
			path = localpath + name  # 定义文件保存路径
			f = open(path, 'wb')  # 打开要保存文件
			filename = 'RETR ' + name  # 保存FTP文件
			self.ftp.retrbinary(filename, f.write)  # 保存FTP上的文件

		self.ftp.set_debuglevel(0)         #关闭调试
		f.close()

	def downloadFile(self, remotedir, filename, localfilepath):
		
		f = open(localfilepath, 'wb')  # 打开要保存文件
		#self.ftp.cwd(remotedir)  # 设置FTP远程目录(路径)
		print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		self.ftp.retrbinary('RETR ' + filename, f.write)  # 保存FTP上的文件
		print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		self.ftp.set_debuglevel(0)
		f.close()

if __name__ == '__main__':
	ftpclient = CFtp()
	ftpclient.connect(host = '127.0.0.1', port = 21, username = 'HikFtpClient' , password = 'Hik666')
	ftpclient.downloadFile("/home/yanggen5/Desktop/WorkDir/source/webservice/bin", "20m.bin", "./20m.bin")
#/home/yanggen5/Desktop/WorkDir/source/webservice/bin



'''
def ftpconnect(host, username, password):
    ftp = FTP()  # 设置变量
    timeout = 30
    port = 21
    ftp.connect(host, port, timeout)  # 连接FTP服务器
    ftp.login(username,password)  # 登录
    return ftp
 
def downloadfile(ftp, remotepath, localpath):
    ftp.cwd(remotepath)  # 设置FTP远程目录(路径)
    list = ftp.nlst()  # 获取目录下的文件,获得目录列表
    for name in list:
        print(name)
        path = localpath + name  # 定义文件保存路径
        f = open(path, 'wb')  # 打开要保存文件
        filename = 'RETR ' + name  # 保存FTP文件
        ftp.retrbinary(filename, f.write)  # 保存FTP上的文件
    ftp.set_debuglevel(0)         #关闭调试
    f.close()                    #关闭文件
'''