from sqlalchemy import create_engine,VARCHAR,Column,BIGINT,DECIMAL,BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import url
engine = create_engine(url) #,echo=True ,print执行的sql


#创建映射
Base = declarative_base(bind=engine)
#创建会话
Session = sessionmaker(bind=engine)
# 定义映射类User，其继承上一步创建的Base
class BaseOperate(object):
    ID = Column(BIGINT,primary_key=True)
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GEOHASH5 = Column(VARCHAR(30))
    GEOHASH7 = Column(VARCHAR(30))
    UNIT_PRICE = Column(VARCHAR(30))
class Operate(BaseOperate,Base):
    __tablename__ = 'operate'
class Operate_1(BaseOperate,Base):
    __tablename__ = 'operate_1'
class OperateParams(Base):
    __tablename__ = 'operate_params'
    ID = Column(BIGINT,primary_key=True)
    GEOHASH = Column(VARCHAR(30))
    LINEAR =  Column(VARCHAR(255))
    LINE_MORE =  Column(VARCHAR(255))
    Ridge = Column(VARCHAR(255))


NetworkSession = sessionmaker(bind=engine)
class Nodes(Base):
    __tablename__ = 'nodes'
    id = Column(BIGINT,primary_key=True)
    osm_id = Column(BIGINT)
    longitude =  Column(DECIMAL(precision=12,scale=9))
    latitude = Column(DECIMAL(precision=12,scale=9))
class Records(Base):
    __tablename__ = 'records'
    id = Column(BIGINT,primary_key=True,autoincrement=True)
    bridge = Column(BOOLEAN)
    oneway =  Column(BOOLEAN)
    tunnel = Column(BOOLEAN)
    ref = Column(VARCHAR(255))
    name = Column(VARCHAR(255))
    code = Column(BIGINT)
    fclass = Column(VARCHAR(255))
    from_node =Column(BIGINT)
    to_node = Column(BIGINT)
