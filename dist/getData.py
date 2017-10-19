import tushare
import datetime
import numpy
import pymysql.cursors

sqluser="root"
sqlpasswd="sjkzyflzsz"

def getDateLine():
	end=datetime.datetime.now()
	start=datetime.datetime.now()+datetime.timedelta(days=-180)
	end=end.strftime("%F")
	start=start.strftime("%F")
	df = tushare.get_k_data("600000", start=start, end=end)
	temp=numpy.array(df)
	data=temp.tolist()
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

	#若已存在则删除表
	cursor.execute("DROP TABLE IF EXISTS dateline")
	#创建表
	sql = """CREATE TABLE dateline (
		id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
		date text,
		open double,
		close double,
		high double,
		low double,
		volume double,
		code text
		)"""

	cursor.execute(sql)

	for i in data:
		 #插入数据
		sql = "INSERT INTO dateline (date,open,close,high,low,volume,code) VALUES (%s,%s,%s,%s,%s,%s,%s)"
		data = ( i[0],i[1],i[2],i[3],i[4],i[5],i[6] )
		sta = cursor.execute(sql,data)
		connect.commit()

	cursor.close()
	 #关闭数据库连接
	connect.close()

def getTodayInfo():
	df = tushare.get_today_all()
	temp=numpy.array(df)
	data=temp.tolist()
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
	#若已存在则删除表
	cursor.execute("DROP TABLE IF EXISTS todayinfo")


	sql = """CREATE TABLE todayinfo (
		id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
		code text,
		name text,
		changepercent double,
		trade double,
		open double,
		high double,
		low double,
		settlement double,
		volume double,
		turnoverratio double,
		amount double,
		per double,
		pb double,
		mktcap double,
		nmc double
		)"""

	cursor.execute(sql)
	for i in data:
		 #插入数据
		sql = "INSERT INTO todayinfo (code,name,changepercent,trade,open,high,low,settlement,volume,turnoverratio,amount,per,pb,mktcap,nmc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		data = ( i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14] )
		sta = cursor.execute(sql,data)
		connect.commit()

	cursor.close()
	 #关闭数据库连接
	connect.close()

def main():
	getDateLine()
	getTodayInfo()

main()
