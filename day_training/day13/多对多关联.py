from sqlalchemy import create_engine,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()  # 生成一个SqlORM 基类(已经封闭metadata)
#echo=True可以查看创建表的过程
engine = create_engine("mysql+pymysql://root:root@localhost:3306/zcl", echo=True)


#直接创建表并返回表的实例  Host2Group主动关联Ｈost与Group(被关联)
Host2Group = Table('host_to_group',Base.metadata,
    Column('host_id',ForeignKey('host.id'),primary_key=True),
    Column('group_id',ForeignKey('group.id'),primary_key=True),
    #一个表为什么能创建两个主键(其实是两个列同时作为主键，非空且唯一)
    #PRIMARY KEY (host_id, group_id),
)


#声明表的映射关系
class Host(Base):
    __tablename__ = 'host'   #表名
    id = Column(Integer, primary_key=True, autoincrement=True) #默认自增
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)
    #外键关联,主机与组名关联
    #group_id = Column(Integer, ForeignKey("group.id"))
    groups = relationship("Group",                #关联Group表
                           secondary = Host2Group, #关联第三方表
                           backref = "host_list")#双向关联，不用在Group类中再加这句代码

    def __repr__(self):
        return "<id=%s,hostname=%s,ip_addr=%s>" % (self.id,
                                                        self.hostname,
                                                        self.ip_addr)

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer,primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    def __repr__(self):
        return "<id=%s,name=%s>" % (self.id, self.name)


Base.metadata.create_all(engine)  # 创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    """
    g1 = Group(name = "g1")
    g2 = Group(name = "g2")
    g3 = Group(name = "g3")
    g4 = Group(name = "g4")
    session.add_all([g1,g2,g3,g4])
    """
    """
    h1 = Host(hostname="h1",ip_addr="10.1.1.1")
    h2 = Host(hostname="h2",ip_addr="10.1.1.2",port=10000)
    h3 = Host(hostname="h3",ip_addr="10.1.1.3",port=6666)
    session.add_all([h1,h2,h3])
    """
    """
    groups = session.query(Group).all()
    h1 = session.query(Host).filter(Host.hostname=="h1").first()
    h1.groups = groups  #将h1关联到所有的组
    print("-->:",h1.groups)
    h1.groups.pop()   #删除一个关联
    """
    h2 = session.query(Host).filter(Host.hostname=="h2").first()
    #h2.groups = groups[1:-1]
    print("=======>h2.groups:",h2.groups)
    #=======>h2.groups: [<__main__.Group object at 0x00000000044A3F98>,
    #  <__main__.Group object at 0x00000000044A3FD0>]
    #加上__repr__()后，变为=======>h2.groups: [<id=2,name=g2>, <id=3,name=g3>]

    g1 = session.query(Group).first()
    print("=======>g1:",g1.host_list)
    #=======>g1: [<id=1,hostname=h1,ip_addr=10.1.1.1>]
    session.commit()