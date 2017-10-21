import tornado.web
import pymysql.cursors
from tornado import escape
import json
import hashlib
import os
import time
import redis
import tushare
import datetime
import numpy
import tushare as ts
from fidata import sqluser,sqlpasswd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



class indexHandler(tornado.web.RequestHandler):#首页处理
	def get(self):#进入首页
		self.render(os.path.join(BASE_DIR, "index.html"))  #进入首页

class ifLoginHandler(tornado.web.RequestHandler):  #判断登录状态
	def post(self):#判断登录状态
		user = self.get_secure_cookie('finance_user')  #获取cookie
		if user:#若user不为空
			user = user.decode()
			r = redis.Redis(host='127.0.0.1', port=6379)
			md = hashlib.md5()
			md.update(user.encode("utf-8"))
			usermd = md.hexdigest()
			session = r.get(user)
			if session:
				if usermd == session.decode():  #判断与redis中存储的信息是否一致
					result = {"state":"true","user":user}
					self.write(result)
		else:
			result = {"state":"false"}
			self.write(result)

class loginHandler(tornado.web.RequestHandler):#处理登录
	def _compare_mysql(self, user, passwd):   #在数据库中比对账户信息
		connect = pymysql.Connect(
	    host='localhost',
	    port=3306,
	    user=sqluser,
	    passwd=sqlpasswd,
	    db='finance',
	    charset='utf8'
		)
	 	#获取游标
		cursor = connect.cursor()

		#查找数据
		sql = "select passwd from userinfo where user = %s"
		data = (user)
		sta = cursor.execute(sql,data)
		cursor.close()
		 #关闭数据库连接
		connect.close()
		result = cursor.fetchone()

		md = hashlib.md5()
		md.update(passwd.encode("utf-8"))
		passwd = md.hexdigest()

		if result == None:
			return False
		else:
			result = result[0]
			if result == passwd:
				return True
			else:
				return False

	def post(self):#判断登录账号密码是否正确
		user = self.get_argument('user')        #接收用户输入的登录账号
		passwd = self.get_argument('passwd')#接收用户输入的登录密码
		if self._compare_mysql(user,passwd):
			print(user, "login")
			result = {"state":"true"}

		else:
			result = {"state":"false"}
		self.write(result)   #返回结果

		md = hashlib.md5()
		md.update(user.encode("utf-8"))
		session = md.hexdigest()
		r = redis.Redis(host='127.0.0.1', port=6379)
		r.set(user,session,ex=3600)    #redis中缓存登录状态
		self.set_secure_cookie('finance_user', user, expires=time.time()+3600)  #cookie中存储用户名，有效时间一小时

class logoutHandler(tornado.web.RequestHandler):#注销
	def post(self):
		user = self.get_argument('user')
		r = redis.Redis(host='127.0.0.1', port=6379)
		r.expire(user,0)
		self.write({"result":"true"})
		print(user,"logout")#注销

class userdataHandler(tornado.web.RequestHandler):#获得用户信息
	def post(self):
		user = self.get_argument('user')
		connect = pymysql.Connect(
	    host='localhost',
	    port=3306,
	    user=sqluser,
	    passwd=sqlpasswd,
	    db='finance',
	    charset='utf8'
		)
	 	#获取游标
		cursor = connect.cursor()
		#查找数据
		sql = "select choose from userinfo where user = %s"
		data = (user)
		sta = cursor.execute(sql,data)
		cursor.close()
		 #关闭数据库连接
		connect.close()

		try:
			choose = cursor.fetchone()
			choose = "".join(choose)    #获取用户自选股
			chooses = choose.split(',')

		r = redis.Redis(host='127.0.0.1', port=6379)
		data = r.get('todayinfo')   #获取所有股票信息
		data = eval(data.decode())

		datachosen = []
		for ele in data:
			if ele.get('code') in chooses:
				datachosen.append(ele)

		self.write({"choose": choose, "state": "true", "data": datachosen})

class todayInfoHandler(tornado.web.RequestHandler):#获得今日A股信息
	def post(self):
		self.write({"result": self._get_data()})

	def _get_data(self):
		r = redis.Redis(host='127.0.0.1', port=6379)
		result = r.get('todayinfo')
		result = eval(result.decode())
		return result

class changechHandler(tornado.web.RequestHandler):#增删自选股
	def post(self):
		user = self.get_argument('user')
		choose = self.get_argument('choose')
		chtype = self.get_argument('type')
		chadd = self.get_argument('chadd')
		chdel = self.get_argument('chdel')
		connect = pymysql.Connect(
	    host='localhost',
	    port=3306,
	    user=sqluser,
	    passwd=sqlpasswd,
	    db='finance',
	    charset='utf8'
		)
	 	#获取游标
		cursor = connect.cursor()
		
		if chtype == 'add':
			if choose.find(chadd)==-1:
				choose += chadd + ','
				self.write({"state":"true"})
			else:
				self.write({"state":"false"})
		elif chtype == 'del':
			if choose.find(chdel)!=-1:
				choose = choose.replace(chdel+',','')
				self.write({"state":"true"})
			else:
				self.write({"state":"false"})
		else:
			self.write({"state":"false"})

		#修改数据
		sql = "update userinfo set choose = %s where user = %s"
		data = (choose,user)
		sta = cursor.execute(sql,data)
		connect.commit()
		cursor.close()
		 #关闭数据库连接
		connect.close()

class klineHandler(tornado.web.RequestHandler):#获取K线图信息
	def post(self):
		code = self.get_argument('code')
		df = ts.get_hist_data(code)
		try:
			index=df.index.values
			temp=numpy.array(index)
			index=temp.tolist()
			data = df.loc[:,['open','close','low','high']]
			temp=numpy.array(data)
			data=temp.tolist()
			self.write({"state":"true","index":index,"data":data})
		except:
			self.write({"state":"false"})

class registerHandler(tornado.web.RequestHandler):#注册
	def post(self):
		user = self.get_argument('user')
		passwd = self.get_argument('passwd')
		connect = pymysql.Connect(
	    host='localhost',
	    port=3306,
	    user=sqluser,
	    passwd=sqlpasswd,
	    db='finance',
	    charset='utf8'
		)
		#获取游标
		cursor = connect.cursor()
		sql = "select user from userinfo"
		cursor.execute(sql)
		result = cursor.fetchone()
		if user in result:
			self.write({"state":"1"})
		else:
			md = hashlib.md5()
			md.update(passwd.encode("utf-8"))
			passwd = md.hexdigest()
			sql = "INSERT INTO userinfo (user,passwd) VALUES (%s,%s)"
			data = (user,passwd)
			cursor.execute(sql,data)
			connect.commit()
			self.write({"state":"0"})
		cursor.close()
		#关闭数据库连接
		connect.close()
		
