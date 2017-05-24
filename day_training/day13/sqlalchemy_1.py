from sqlalchemy import create_engine

#连接数据库，生成engine对象；最大连接数为５个
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/zcl", max_overflow=5)
print(engine)   #Engine(mysql+pymysql://root:***@127.0.0.1:3306/zcl)
result = engine.execute('select * from students') #不用commit(),会自动commit
print(result.fetchall())

