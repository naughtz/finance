import pymysql.cursors
import redis


def readTodayInfo():#将todayinfo缓存入redis
	connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='sjkzyflzsz',
    db='finance',
    charset='utf8',
	cursorclass=pymysql.cursors.DictCursor
	)
	#获取游标
	cursor = connect.cursor()
	#查找数据
	sql = "select * from todayinfo"
	cursor.execute(sql)
	cursor.close()
	 #关闭数据库连接
	connect.close()
	result = cursor.fetchall()
	r = redis.Redis(host='127.0.0.1', port=6379)
	r.set('todayinfo',result)