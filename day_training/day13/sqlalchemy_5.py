from sqlalchemy import create_engine,func
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


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer,primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


Base.metadata.create_all(engine)  # 创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    # obj = session.query(Host).join(Host.group).all()  #相当于inner join
    # print("-->obj:",obj)

    obj1 = session.query(Host).join(Host.group).group_by(Group.name).all()
    print("-->obj1:",obj1)
    #需要导入from sqlalchemy import func
    obj2 = session.query(Host,func.count(Group.name)).join(Host.group).group_by(Group.name).all()
    print("-->obj2:",obj2)
    session.commit()