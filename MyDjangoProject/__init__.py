import pymysql
from DBUtils.PooledDB import PooledDB
pymysql.install_as_MySQLdb()


#打开数据库连接
# db = pymysql.connect("localhost","root","root","test")
#db=pymysql.connect(user='root',db='test',passwd='root',host='localhost',charset='utf8')

#使用cursor获取操作游标
#cursor = db.cursor()
#使用excute方法执行SQL语句
# cursor.execute("SELECT VERSION()")


#使用fetchone方法获取一条数据
# data = cursor.fetchall()
# print(data)

def createPool():
    pool = PooledDB(pymysql, 50, host='localhost', user='root', passwd='root', db='test', port=3306,
                    charset='utf8')  # 50为连接池里的最少连接数
    return pool

def selectSQL():
    pool = createPool()
    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cursor = conn.cursor()
    data = cursor.execute("select *from user")
    info = cursor.fetchmany(data)
    cursor.close()
    conn.close()
    pool.close()
    return info

