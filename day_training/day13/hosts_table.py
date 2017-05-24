from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # 生成一个SqlORM 基类(已经封闭metadata)
#echo=True可以查看创建表的过程
engine = create_engine("mysql+pymysql://root:root@localhost:3306/zcl", echo=True)

class Host(Base):
    __tablename__ = 'hosts'   #表名
    id = Column(Integer, primary_key=True, autoincrement=True) #默认自增
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)
    #外键关联
    group_id = Column(Integer, ForeignKey("group.id"))

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer,primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


Base.metadata.create_all(engine)  # 创建所有表结构
#
if __name__ == '__main__':
    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()  #连接的实例
#     #准备插入数据
#     h1 = Host(hostname='localhost',ip_addr='127.0.0.1')  #实例化(未创建)
#     h2 = Host(hostname='ubuntu',ip_addr='192.168.2.243',port=20000)
#
#     # session.add(h１)　　　#也可以用下面的批量处理
#     # session.add_all([h1,h2])
#     # h2.hostname = 'ubuntu_test' #只要没提交,此时修改也没问题
#     # session.rollback()
#     #查询数据，返回一个对象
#     obj = session.query(Host).filter(Host.hostname=="localhost").first()
#     print("-->",obj)
#     #[<__main__.Host object at 0x00000000048DC0B8>] 如果上面为.all()
#     #<__main__.Host object at 0x000000000493C208>  如果上面为.first()
#
#     # 如果用.all(),会曝错AttributeError: 'list' object has no attribute 'hostname'
#     #obj.hostname = "localhost"
#
#     session.delete(obj)  #删除行
#
    session.commit() #提交
