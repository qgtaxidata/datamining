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
#属于排行榜的数据表，可以忽略
class OperateRevenue1(Base):
    __tablename__ = 'operate_his1'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue2(Base):
    __tablename__ = 'operate_his2'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue3(Base):
    __tablename__ = 'operate_his3'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue4(Base):
    __tablename__ = 'operate_his4'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue5(Base):
    __tablename__ = 'operate_his5'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue6(Base):
    __tablename__ = 'operate_his6'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue7(Base):
    __tablename__ = 'operate_his7'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue8(Base):
    __tablename__ = 'operate_his8'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue9(Base):
    __tablename__ = 'operate_his9'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue10(Base):
    __tablename__ = 'operate_his10'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue11(Base):
    __tablename__ = 'operate_his11'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue12(Base):
    __tablename__ = 'operate_his12'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue13(Base):
    __tablename__ = 'operate_his13'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue14(Base):
    __tablename__ = 'operate_his14'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue15(Base):
    __tablename__ = 'operate_his15'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue16(Base):
    __tablename__ = 'operate_his16'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue17(Base):
    __tablename__ = 'operate_his17'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue18(Base):
    __tablename__ = 'operate_his18'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue19(Base):
    __tablename__ = 'operate_his19'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))
class OperateRevenue20(Base):
    __tablename__ = 'operate_his20'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))

# 新增：
class OperateRevenue21(Base):
    __tablename__ = 'operate_his21'
    ID = Column(BIGINT,primary_key=True)
    EQUIPMENT_ID = Column(VARCHAR(30))
    PLATENO = Column(VARCHAR(24))
    COMPANY_ID = Column(VARCHAR(10))
    TEAM_CODE = Column(VARCHAR(8))
    EMPTY_MILE = Column(VARCHAR(24))
    EMPTY_BEGIN_TIME = Column(VARCHAR(255))
    WORK_BEGIN_TIME = Column(VARCHAR(255))
    WORK_END_TIME = Column(VARCHAR(255))
    UNIT_PRICE = Column(VARCHAR(7))
    LOAD_MILE = Column(VARCHAR(6))
    SLOW_COUNT_TIME = Column(VARCHAR(11))
    OPERATE_MONEY = Column(VARCHAR(20))
    EVALUATE = Column(VARCHAR(11))
    TRADE_CODE = Column(VARCHAR(96))
    GET_ON_LONGITUDE = Column(VARCHAR(16))
    GET_ON_LATITUDE = Column(VARCHAR(16))
    GET_OFF_LONGITUDE = Column(VARCHAR(16))
    GET_OFF_LATITUDE = Column(VARCHAR(16))
    TIME_REPRE = Column(VARCHAR(11))
    GEOHASH5 = Column(VARCHAR(30))
    MIN_REPRE = Column(VARCHAR(11))
    GEOHASH7 = Column(VARCHAR(30))
    GEOEND7 = Column(VARCHAR(765))
    CHAUFFEUR_NO = Column(VARCHAR(8))
    ROW_KEY = Column(VARCHAR(120))

class OperateRevenueRanking(Base):
    __tablename__ = 'revenue_ranking'
    day = Column(VARCHAR(255), primary_key=True)
    Admin = Column(VARCHAR(5))
    ranking = Column(VARCHAR(255))

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


class New_Income_Table(Base):
    __tablename__ = 'DIST_INCOME'
    ID =  Column(BIGINT,primary_key=True)
    AREA = Column(VARCHAR(30))
    INCOME = Column(VARCHAR(20))
    BEGIN_TIME = Column(VARCHAR(255))
    END_TIME = Column(VARCHAR(255))


class new_table_for_hot(Base):
    __tablename__ = 'HOT_INFO'
    ID =  Column(BIGINT,primary_key=True)
    geohash5 = Column(VARCHAR(20))
    period = Column(VARCHAR(225))
    total_income = Column(VARCHAR(30))
    empty_mile = Column(VARCHAR(30))
    show_speed = Column(VARCHAR(20))
    count = Column(BIGINT)

