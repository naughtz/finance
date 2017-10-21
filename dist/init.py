import pymysql
from fidata import sqluser,sqlpasswd

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

cursor.execute("CREATE DATABASE IF NOT EXISTS finance")
sql = """CREATE TABLE userinfo (
		user char(20),
		passwd varchar(100),
		choose text,
		)"""
cursor.execute(sql)
connect.commit()
cursor.close()
#关闭数据库连接
connect.close()
