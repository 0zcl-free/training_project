import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='zcl')
cur = conn.cursor()

reCount = cur.execute('select* from students')

res = cur.fetchone()       #获取一条数据
res2 = cur.fetchmany(3)   #获取3条数据
res3 = cur.fetchall()     #获取所有(元组格式)
print(res)
print(res2)
print(res3)
conn.commit()

cur.close()
conn.close()

# print
# reCount
#
# # ############################## fetchall  ##############################
#
# import MySQLdb
#
# conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='1234', db='mydb')
# # cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
# cur = conn.cursor()
#
# reCount = cur.execute('select Name,Address from UserInfo')
#
# nRet = cur.fetchall()
#
# cur.close()
# conn.close()
#
# print
# reCount
# print
# nRet
# for i in nRet:
#     print
#     i[0], i[1]