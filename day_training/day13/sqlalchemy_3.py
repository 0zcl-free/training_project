from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey,select

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             )

color = Table('color', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              )
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/zcl", max_overflow=5)

conn = engine.connect()  #创建游标,当前实例所处状态

# 创建SQL语句，INSERT INTO "user" (id, name) VALUES (:id, :name)
#id号可省略，是自增的
# conn.execute(user.insert(), {'id': 1, 'name': 'zcl'})
# conn.close()

# sql = user.insert().values(name='wu')  #插入
# conn.execute(sql)
# conn.close()

#删除id号大于１的行,也可以where(user.c.name=="zcl")
# sql = user.delete().where(user.c.id > 1)
# conn.execute(sql)
# conn.close()

# 将name=="wuu"更改为"name=="ed"
# sql = user.update().where(user.c.name == 'wuu').values(name='ed')
# conn.execute(sql)
# conn.close()

#查询
#sql = select([user, ])  #[(1, 'zcl'), (9, 'ed'), (10, 'ed')]
# sql = select([user.c.id, ])   #[(1,), (9,), (10,)]
sql = select([user.c.name, color.c.name]).where(user.c.id==color.c.id)
# sql = select([user.c.name]).order_by(user.c.name)
# sql = user.select([user]).group_by(user.c.name)

result = conn.execute(sql)
print(result.fetchall())
conn.close()