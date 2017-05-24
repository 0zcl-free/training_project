

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()  # 生成一个SqlORM 基类(已经封闭metadata)
#echo=True可以查看创建表的过程
engine = create_engine("mysql+pymysql://root:root@localhost:3306/zcl", echo=True)

class Host(Base):
    __tablename__ = 'hosts'   #表名
    id = Column(Integer, primary_key=True, autoincrement=True) #默认自增
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)
    #外键关联,主机与组名关联
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", backref = "host_list")
    #group = relationship("Group", back_populates = "host_list")

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer,primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    #hosts = relationship("Host")

Base.metadata.create_all(engine)  # 创建所有表结构

if __name__ == '__main__':
    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()  #连接的实例

    g1 = Group(name = "g1")
    g2 = Group(name = "g2")
    g3 = Group(name = "g3")
    g4 = Group(name = "g4")
    session.add_all([g1,g2,g3,g4])

    g4 = session.query(Group).filter(Group.name=="g4").first()
    h = session.query(Host).filter(Host.hostname=="localhost").first()
    print("h1:",h.group_id)
    #此时可以获取已经关联的group_id，但如何获取已关联的组的组名
    print(h.group.name)#AttributeError: 'Host' object has no attribute 'group'
    print("g4:",g4.host_list) #g4: [<__main__.Host object at 0x0000000004303860>]

    #此时上面的g1,g2,g3三条记录还未存在，g1.id也未存在，运行时虽然不曝错，但关联不成功
    h1 = Host(hostname='localhost', ip_addr='127.0.0.1',group_id=g1.id)
    session.add(h1)

    session.commit() #提交
