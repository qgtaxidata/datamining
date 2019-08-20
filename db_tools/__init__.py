from db_tools.base_table import *
from datetime import datetime


def income_info(day, geohash, time_):
    session = Session()
    lst = []
    if day == '2017-02-03':
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY)/100])
    elif day == '2017-02-04':
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-05':
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-06':
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-13':
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-14':
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-15':
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-16':
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-17':
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-18':
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-19':
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-20':
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    elif day == '2017-02-21':
        for col in session.query(OperateRevenue21).filter(OperateRevenue21.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY) / 100])

    session.close()
    return list(lst)


def insert_income_info(AREA,INCOME, BEGIN_TIME, END_TIME):
    session = Session()
    p = New_Income_Table(AREA = AREA,INCOME = INCOME, BEGIN_TIME = BEGIN_TIME,END_TIME = END_TIME)
    session.add(p)
    session.commit()
    session.close()


def get_info_of_income(area, date):
    session = Session()
    lst = []
    for col in session.query(New_Income_Table).filter(New_Income_Table.AREA == area,).all():
        if col.BEGIN_TIME == date:
            # print("haha",[col.INCOME,[col.BEGIN_TIME,col.END_TIME]])
            lst.extend([float(col.INCOME),[col.BEGIN_TIME,col.END_TIME]])
    session.close()
    return lst


def get_date_time(strs):
    return datetime.strptime(strs,'%Y-%m-%d %H:%M:%S')

def query_taxi_pos(table_itr =(1,)):
    _engine = create_engine('mysql+pymysql://qgtaxi:qgtaxi_2018@10.21.48.11/taxilog')  # ,echo=True ,print执行的sql
    _Base = declarative_base(bind=_engine)
    Session = sessionmaker(bind=_engine)
    for i in table_itr:
        exec(f'''class _TaxiPos{i}(BaseTaxiPos,_Base):
        __tablename__ = "gpsdata{i}"''')
    s = Session()
    for i in table_itr:
        c = eval('_TaxiPos'+str(i))   #映射单个表的类
        q = s.query(c)
        for i,col in enumerate(s.query(c).order_by(c.GPS_TIME).limit(1e4).yield_per(1000)): #.limit(1e3)): #
            # print(i)
            GPS_TIME = col.GPS_TIME
            LATITUDE = col.LATITUDE
            LONGITUDE = col.LONGITUDE
            LICENSEPLATENO = col.LICENSEPLATENO
            yield [LICENSEPLATENO, GPS_TIME, LONGITUDE, LATITUDE]


def query_operate_pos(begin_time_l,geohase5,delta=3600):
    '''
     :param begin_time_l:str,like: '2017-02-01 19:0:47'
     :param geohase7: str
     :param delta: int
     :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    day = begin_time_l[0:10]
    #input(day)
    if day == '2017-02-03':
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-04':
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-05':
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-06':
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])


    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-13':
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-14':
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-15':
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-16':
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])


    elif day == '2017-02-17':
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-18':
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-19':
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    elif day == '2017-02-20':
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])


    elif day == '2017-02-21':
        for col in session.query(OperateRevenue21).filter(OperateRevenue21.GEOHASH5 == geohase5).all():
            if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
                lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)])

    session.close()
    return list(lst)


def query_operate(begin_time_l, geohase5, delta=3600):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase5: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate).filter(Operate.GEOHASH5 == geohase5).all():
        if (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
            lst.append([float(col.GET_ON_LONGITUDE),float(col.GET_ON_LATITUDE)])
    session.close()
    return lst


def query_operate_price(begin_time_l,geohase7,delta=600):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate).filter(Operate.GEOHASH7 == geohase7).all():
        if 0< (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
            lst.append(float(col.UNIT_PRICE))
    session.close()
    return lst

def query_operate_price_1(begin_time_l,geohase7,delta=600):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate_1).filter(Operate_1.GEOHASH7 == geohase7).all():
        if (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
            lst.append(float(col.UNIT_PRICE))
    session.close()
    return lst

def query_operate_price_del(begin_time_l,geohase5,delta=1):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate_1).filter(Operate_1.GEOHASH5 == geohase5).all():
        if (delta-1)*300 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta*300:
            lst.append(float(col.UNIT_PRICE))
    session.close()
    return lst
def query_operate_geohash():
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate_1).all():
        lst.append(col.GEOHASH5)
    session.close()
    return lst

def insert_operate_params(GEOHASH,LINEAR,LINE_MORE,RIDGE):
    session = Session()
    p = OperateParams(GEOHASH=GEOHASH,
                  LINEAR=LINEAR,LINE_MORE=LINE_MORE,Ridge=RIDGE)
    session.add(p)
    session.commit()
    session.close()

def get_operate_params(geohash):
    session = Session()
    lst = []
    for col in session.query(OperateParams).filter(OperateParams.GEOHASH == geohash).all():
        lst.append([col.LINEAR, col.LINE_MORE, col.Ridge])
    session.close()
    return lst

# gps轨迹数据
def query_taxi_qua(firstid,table_itr=(13,),win=100000):
    _engine = create_engine('mysql+pymysql://qgtaxi:qgtaxi_2018@10.21.48.11/taxilog')  # ,echo=True ,print执行的sql
    _Base = declarative_base(bind=_engine)
    Session = sessionmaker(bind=_engine)
    for i in table_itr:
        exec(f'''class _TaxiPos{i}(BaseTaxiPos,_Base):
        __tablename__ = "gpsdata_copy{i}"''')
    s = Session()
    for i in table_itr:
        cls = eval('_TaxiPos'+str(i))   #映射单个表的类
        pk_attr = cls.ID
        qry = s.query(cls)
        q = qry.filter(pk_attr> firstid).filter(pk_attr < firstid+ win).filter(cls.CAR_STAT1!='7')  #熄火部分不计
        for col in q.order_by(cls.GPS_TIME):     #.limit(win):
            GPS_TIME = col.GPS_TIME
            HOUR_REPRE =col.HOUR_REPRE
            LATITUDE = col.LATITUDE
            LONGITUDE = col.LONGITUDE
            LICENSEPLATENO = col.LICENSEPLATENO
            yield [LICENSEPLATENO,HOUR_REPRE, GPS_TIME, LONGITUDE, LATITUDE]
        return None

def query_zone_quality(gZone,hour):
    s = Session()
    inst = s.query(ZoneQuality).filter(ZoneQuality.g_zone==gZone).filter(ZoneQuality.hour_repre==str(hour)).first()
    return float(inst.average_time),float(inst.density),float(inst.flow)


# 这部分代码属于收入排行榜使用的算法，故可以注释
def get_operate_his(day):
    session = Session()
    lst = []
    if day == 3:
        for col in session.query(OperateRevenue3).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 4:
        for col in session.query(OperateRevenue4).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 5:
        for col in session.query(OperateRevenue5).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 6:
        for col in session.query(OperateRevenue6).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 7:
        for col in session.query(OperateRevenue7).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 8:
        for col in session.query(OperateRevenue8).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 9:
        for col in session.query(OperateRevenue9).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 10:
        for col in session.query(OperateRevenue10).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 11:
        for col in session.query(OperateRevenue11).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 12:
        for col in session.query(OperateRevenue12).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 13:
        for col in session.query(OperateRevenue13).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 14:
        for col in session.query(OperateRevenue14).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 15:
        for col in session.query(OperateRevenue15).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 16:
        for col in session.query(OperateRevenue16).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 17:
        for col in session.query(OperateRevenue17).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 18:
        for col in session.query(OperateRevenue18).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 19:
        for col in session.query(OperateRevenue19).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 20:
        for col in session.query(OperateRevenue20).all():
            lst.append(col.CHAUFFEUR_NO)
    session.close()
    return list(set(lst))

def get_operate_revenue(drive, geohash, day):
    session = Session()
    lst = []
    if day == 3:
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.CHAUFFEUR_NO == drive).filter(OperateRevenue3.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 4:
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.CHAUFFEUR_NO == drive).filter(OperateRevenue4.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 5:
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.CHAUFFEUR_NO == drive).filter(OperateRevenue5.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 6:
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.CHAUFFEUR_NO == drive).filter(OperateRevenue6.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 7:
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.CHAUFFEUR_NO == drive).filter(OperateRevenue7.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 8:
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.CHAUFFEUR_NO == drive).filter(OperateRevenue8.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 9:
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.CHAUFFEUR_NO == drive).filter(OperateRevenue9.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 10:
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.CHAUFFEUR_NO == drive).filter(OperateRevenue10.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 11:
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.CHAUFFEUR_NO == drive).filter(OperateRevenue11.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 12:
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.CHAUFFEUR_NO == drive).filter(OperateRevenue12.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 13:
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.CHAUFFEUR_NO == drive).filter(OperateRevenue13.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 14:
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.CHAUFFEUR_NO == drive).filter(OperateRevenue14.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 15:
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.CHAUFFEUR_NO == drive).filter(OperateRevenue15.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 16:
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.CHAUFFEUR_NO == drive).filter(OperateRevenue16.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 17:
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.CHAUFFEUR_NO == drive).filter(OperateRevenue17.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    elif day == 18:
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.CHAUFFEUR_NO == drive).filter(OperateRevenue18.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 19:
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.CHAUFFEUR_NO == drive).filter(OperateRevenue19.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    elif day == 20:
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.CHAUFFEUR_NO == drive).filter(OperateRevenue20.GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
    session.close()
    lst = list(set([tuple(t) for t in lst]))
    all_list = []
    for i in range(len(lst)):
        all_list.append(lst[i][1])
    return list(all_list)

def get_drive_operste(geohash, day):
    session = Session()
    lst = []
    if day == 3:
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 4:
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 5:
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 6:
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 7:
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 8:
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 9:
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 10:
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 11:
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 12:
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 13:
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 14:
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 15:
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 16:
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 17:
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 18:
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 19:
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    elif day == 20:
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH5 == geohash).all():
            lst.append(col.CHAUFFEUR_NO)
    session.close()
    lst = list(set(lst))
    return lst

def get_operate_order(geo_):
    session = Session()
    total_order = []
    d0 = [];d1 = [];d2 = [];d3 = [];d4 = [];d5 = [];d6 = [];d7 = [];d8 = [];d9 = [];d10 = []
    for col in session.query(OperateRevenue3).all():
        if col.GEOHASH5 in geo_[0]:
            d0.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[1]:
            d1.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[2]:
            d2.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[3]:
            d3.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[4]:
            d4.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[5]:
            d5.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[6]:
            d6.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[7]:
            d7.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[8]:
            d8.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[9]:
            d9.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
        if col.GEOHASH5 in geo_[10]:
            d10.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
    total_order.append(d0)
    total_order.append(d1)
    total_order.append(d2)
    total_order.append(d3)
    total_order.append(d4)
    total_order.append(d5)
    total_order.append(d6)
    total_order.append(d7)
    total_order.append(d8)
    total_order.append(d9)
    total_order.append(d10)
    session.close()
    # input(total_order[0])
    return total_order

def insert_operate_ranking(day, Admin, ranking):
    session = Session()
    p = OperateRevenueRanking(day=day, Admin=Admin, ranking=ranking)
    session.add(p)
    session.commit()
    session.close()

#得到收入排行榜
def get_operate_rank(area, day):
    session = Session()
    lst = []
    for col in session.query(OperateRevenueRanking).filter(OperateRevenueRanking.day == day).filter(OperateRevenueRanking.Admin == area).all():
        lst.append(eval(col.ranking))
    session.close()
    return lst

#负责查询在一定天数内的司机的各个信息
def get_drive_information(driver_count, day, geohash):
    session = Session()
    lst = []
    if day == 3:
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.CHAUFFEUR_NO == driver_count).filter(OperateRevenue3.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 4:
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.CHAUFFEUR_NO == driver_count).filter(OperateRevenue4.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 5:
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.CHAUFFEUR_NO == driver_count).filter(OperateRevenue5.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 6:
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.CHAUFFEUR_NO == driver_count).filter(OperateRevenue6.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 7:
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.CHAUFFEUR_NO == driver_count).filter(OperateRevenue7.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 8:
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.CHAUFFEUR_NO == driver_count).filter(OperateRevenue8.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 9:
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.CHAUFFEUR_NO == driver_count).filter(OperateRevenue9.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 10:
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.CHAUFFEUR_NO == driver_count).filter(OperateRevenue10.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 11:
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.CHAUFFEUR_NO == driver_count).filter(OperateRevenue11.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 12:
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.CHAUFFEUR_NO == driver_count).filter(OperateRevenue12.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 13:
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.CHAUFFEUR_NO == driver_count).filter(OperateRevenue13.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 14:
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.CHAUFFEUR_NO == driver_count).filter(OperateRevenue14.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 15:
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.CHAUFFEUR_NO == driver_count).filter(OperateRevenue15.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 16:
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.CHAUFFEUR_NO == driver_count).filter(OperateRevenue16.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 17:
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.CHAUFFEUR_NO == driver_count).filter(OperateRevenue17.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 18:
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.CHAUFFEUR_NO == driver_count).filter(OperateRevenue18.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 19:
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.CHAUFFEUR_NO == driver_count).filter(OperateRevenue19.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 20:
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.CHAUFFEUR_NO == driver_count).filter(OperateRevenue20.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 21:
        for col in session.query(OperateRevenue21).filter(OperateRevenue21.CHAUFFEUR_NO == driver_count).filter(OperateRevenue21.GEOHASH5==geohash).all():
            lst.append([col.COMPANY_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    session.close()
    lst = list(set([tuple(t) for t in lst]))
    all_list = []
    for i in range(len(lst)):
        all_list.append(list(lst[i]))
    return list(all_list)


#负责查询在一定天数内的订单的各个信息(计算一个区的频率，一个区的）
def get_order_information(day, geohash, time_):
    session = Session()
    lst = []
    if day == '2017-02-01':
        for col in session.query(OperateRevenue1).filter(OperateRevenue1.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-02':
        for col in session.query(OperateRevenue2).filter(OperateRevenue2.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-03':
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-04':
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-05':
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-06':
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-13':
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-14':
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-15':
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-16':
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-17':
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-18':
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-19':
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-20':
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    elif day == '2017-02-21':
        for col in session.query(OperateRevenue21).filter(OperateRevenue21.GEOHASH5==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME])
    session.close()
    lst = list(set([tuple(t) for t in lst]))
    all_list = []
    for i in range(len(lst)):
        all_list.append(list(lst[i]))
    return list(all_list)

def insert_efficie_paramers(area, strat_time, end_time, mile_efficiency, time_efficiency, total_drive_num):
    session = Session()
    p = Operateefficient(area=area, start_time=strat_time, end_time=end_time, mile_efficiency=mile_efficiency, time_efficiency=time_efficiency, total_drive_num=total_drive_num)
    session.add(p)
    session.commit()
    session.close()

def get_efficiencyPredict(area, day):
    session = Session()
    lst = []
    for col in session.query(Operateefficient).filter(Operateefficient.area == area).filter(Operateefficient.start_time == day[0]).filter(Operateefficient.end_time == day[1]).all():
        lst.append([float(col.mile_efficiency), float(col.time_efficiency), int(col.total_drive_num), [col.start_time, col.end_time]])
    session.close()
    return lst[0]


def insert_Operatehotdata(date, geohash, times, number):
    session = Session()
    p = Operatehotdata(date=date, geohash=geohash, times=times,number=number)
    session.add(p)
    session.commit()
    session.close()

def get_Operatehotdata(date, geohash):
    session = Session()
    lst = []
    for col in session.query(Operatehotdata).filter(Operatehotdata.date == date).filter(
            Operatehotdata.geohash == geohash).all():
        lst.append(col.number)
    session.close()
    return lst

def get_Operatehotdata7(date, geohash):
    session = Session()
    lst = []
    for col in session.query(Operatehotdata7).filter(Operatehotdata7.date == date).filter(
            Operatehotdata7.geohash7 == geohash).all():
        lst.append(col.number)
    session.close()
    return lst

#负责查询在一定天数内的订单的各个信息(计算一个区的频率，一个区的）
def get_order_information7(day, geohash, time_):
    session = Session()
    lst = []
    if day == '2017-02-01':
        for col in session.query(OperateRevenue1).filter(OperateRevenue1.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-02':
        for col in session.query(OperateRevenue2).filter(OperateRevenue2.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-03':
        for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-04':
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-05':
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-06':
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-13':
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-14':
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-15':
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-16':
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-17':
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-18':
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-19':
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-20':
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    elif day == '2017-02-21':
        for col in session.query(OperateRevenue21).filter(OperateRevenue21.GEOHASH7==geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append(float(col.LOAD_MILE))
    session.close()
    # lst = list(set([tuple(t) for t in lst]))
    # all_list = []
    # for i in range(len(lst)):
    #     all_list.append(list(lst[i]))
    return lst

def query_operate_geohash7():
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(OperateRevenue3).all():
        lst.append(col.GEOHASH7)
    for col in session.query(OperateRevenue4).all():
        lst.append(col.GEOHASH7)
    for col in session.query(OperateRevenue5).all():
        lst.append(col.GEOHASH7)
    for col in session.query(OperateRevenue6).all():
        lst.append(col.GEOHASH7)
    for col in session.query(OperateRevenue7).all():
        lst.append(col.GEOHASH7)
    session.close()
    return lst

def get_passage(day):
    session = Session()
    lst_car = []
    lst_passager = []
    if day == '2017-02-06':
        for col in session.query(OperateRevenue6).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).all():
            lst_passager.append(col.CHAUFFEUR_NO)
            lst_car.append(col.PLATENO)
    session.close()
    return list(set(lst_car)), list(set(lst_passager))


def get_driver_fre(day, drvie_number):
    session = Session()
    lst_passager = []
    if day == '2017-02-06':
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.CHAUFFEUR_NO == drvie_number).all():
            lst_passager.append(col.WORK_BEGIN_TIME)
    session.close()
    return lst_passager

def get_hot_info_1(get_):
    session = Session()
    lst = []
    for col in session.query(new_table_for_hot).all():
        if col.geohash5 in get_:
            lst.append([col.geohash5, col.period, col.total_income,col.empty_mile,col.show_speed,col.count])
    session.close()
    return lst

def get_hot_info_2(get_,date_):
    session = Session()
    lst = []
    day = date_[0:10]
    day1 = date_[0:14] + '00:00'
    day2 = (get_date_time(str(day1)) + timedelta(hours = 1))
    # print(day,day1,day2)
    if day == '2017-02-01':
        for col in session.query(OperateRevenue1).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-02':
        for col in session.query(OperateRevenue2).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE), str(col.SLOW_COUNT_TIME)])
    elif day == '2017-02-03':
        for col in session.query(OperateRevenue3).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
    elif day == '2017-02-04':
        for col in session.query(OperateRevenue4).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-05':
        for col in session.query(OperateRevenue5).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-06':
        for col in session.query(OperateRevenue6).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-07':
        for col in session.query(OperateRevenue7).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-08':
        for col in session.query(OperateRevenue8).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-09':
        for col in session.query(OperateRevenue9).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
    elif day == '2017-02-10':
        for col in session.query(OperateRevenue10).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-11':
        for col in session.query(OperateRevenue11).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-12':
        for col in session.query(OperateRevenue12).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-13':
        for col in session.query(OperateRevenue13).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-14':
        for col in session.query(OperateRevenue14).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
# 修改
    elif day == '2017-02-15':
        for col in session.query(OperateRevenue15).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
    elif day == '2017-02-16':
        for col in session.query(OperateRevenue16).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-17':
        for col in session.query(OperateRevenue17).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-18':
        for col in session.query(OperateRevenue18).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])

    elif day == '2017-02-19':
        for col in session.query(OperateRevenue19).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
    elif day == '2017-02-20':
        for col in session.query(OperateRevenue20).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
    elif day == '2017-02-21':
        for col in session.query(OperateRevenue21).all():
            if int(str(col.WORK_BEGIN_TIME)[11:13]) == int(str(date_)[11:13]):
                if col.GEOHASH5 in get_:
                    lst.append([col.GEOHASH5, str(float(col.OPERATE_MONEY) / 100), str(col.EMPTY_MILE),
                                str(col.SLOW_COUNT_TIME)])
    test_dict = {}
    # 对lst进行整理
    for i in range(len(lst)):
        if lst[i][0] not in test_dict.keys():
            test_dict[lst[i][0]] = []
        test_dict[lst[i][0]].append(lst[i])
    # 对字典进行处理：
    one_geo = []
    for key in test_dict.keys():
        one_geo.append([key,str([str(day1), str(day2)]),sum([float(i[1]) for i in test_dict[key]]),sum([float(i[2]) for i in test_dict[key]]),sum([float(i[3]) for i in test_dict[key]]),len(test_dict[key])])
    session.close()
    return one_geo[0]



if __name__ =='__main__':
    geohase7='ws0e9u4'
    begin_time_l ='2017-02-01 0:0:0'
    begin_time_u = '2017-02-02 19:53:47'
    # lst = query_operate(begin_time_l,geohase7)
    # lst = query_operate_(begin_time_l,begin_time_u,None)
