from sqlalchemy import create_engine, \
    Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()  #相当于实例一个父类

user = Table('user', metadata,      #相当于让Table继承metadata类
             Column('id', Integer, primary_key=True),
             Column('name', String(20)),
             )

color = Table('color', metadata,    #表名color
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              )
engine = create_engine("mysql+pymysql://root:root@localhost:3306/zcl", max_overflow=5)

metadata.create_all(engine)  #table已经与metadate绑定