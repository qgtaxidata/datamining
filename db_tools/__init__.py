from sqlalchemy import create_engine,VARCHAR,Column,BIGINT,DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from db_tools.settings import url

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


def get_date_time(strs):
    return datetime.strptime(strs,'%Y-%m-%d %H:%M:%S')

def query_operate(begin_time_l,geohase7,delta=30):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate).filter(Operate.GEOHASH7 == geohase7).all():
        if (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
            lst.append([float(col.GET_ON_LONGITUDE),float(col.GET_ON_LATITUDE)])
    session.close()
    return lst

def query_operate_command(begin_time_l,geohase7,delta=600):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate).filter(Operate.GEOHASH7 == geohase7).all():
        if (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
            lst.append(float(col.UNIT_PRICE))
    session.close()
    return lst



def query_operate_(begin_time_l,begin_time_u,geohase7):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param begin_time_u: str
    :param geohase7: str
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    if geohase7 is None:
        for col in session.query(Operate).all():
            if get_date_time(begin_time_l) <= get_date_time(col.WORK_BEGIN_TIME) <= get_date_time(begin_time_u):
                WORK_BEGIN_TIME = col.WORK_BEGIN_TIME.split(' ',1)[1]
                WORK_END_TIME = col.WORK_END_TIME.split(' ',1)[1]
                lst.append([col.GET_ON_LONGITUDE,col.GET_ON_LATITUDE,WORK_BEGIN_TIME,WORK_END_TIME])
    else:
        for col in session.query(Operate).filter(Operate.GEOHASH7 == geohase7).all():
            if get_date_time(begin_time_l) <= get_date_time(col.WORK_BEGIN_TIME) <= get_date_time(begin_time_u):
                WORK_BEGIN_TIME = col.WORK_BEGIN_TIME.split(' ',1)[1]
                WORK_END_TIME = col.WORK_END_TIME.split(' ',1)[1]
                lst.append([col.GET_ON_LONGITUDE,col.GET_ON_LATITUDE,WORK_BEGIN_TIME,WORK_END_TIME])
    session.close()
    return lst


if __name__ =='__main__':
    geohase7='ws0e9u4'
    begin_time_l ='2017-02-01 0:0:0'
    begin_time_u = '2017-02-02 19:53:47'
    # lst = query_operate(begin_time_l,geohase7)
    # lst = query_operate_(begin_time_l,begin_time_u,None)
    # with open('lst.py','w') as f:
    #     f.write(str(lst))