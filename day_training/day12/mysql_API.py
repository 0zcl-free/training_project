
import pymysql
#连接数据库zcl
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='zcl')
#生成游标，当前实例所处状态
cur = conn.cursor()
li = [
    ("cjy","man",18,1562234,"USA"),
    ("cjy2","man",18,1562235,"USA"),
    ("cjy3","man",18,1562235,"USA"),
    ("cjy4","man",18,1562235,"USA"),
    ("cjy5","man",18,1562235,"USA"),
]

#插入数据
reCount = cur.executemany('insert into students(name,sex,age,tel,nal) values(%s,%s,%s,%s,%s)', li)

#conn.rollback()  #事务回滚
conn.commit()  #实例提交命令

cur.close()
conn.close()
print(reCount)
