import tushare
import datetime
import numpy
import pymysql.cursors
from fidata import sqluser,sqlpasswd


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
	getTodayInfo()

main()
