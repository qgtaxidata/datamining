from db_tools.base_table import *
from datetime import datetime,timedelta

def get_date_time(strs):
    return datetime.strptime(strs,'%Y-%m-%d %H:%M:%S')
#
# def query_operate_pos(begin_time_l,geohase7,delta=30):
#     '''
#     :param begin_time_l:str,like: '2017-02-01 19:0:47'
#     :param geohase7: str
#     :param delta: int
#     :return: [[lon,lat]]
#     '''
#     session = Session()
#     lst = []
#     for col in session.query(Operate).filter(Operate.GEOHASH7 == geohase7).all():
#         if (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
#             lst.append([float(col.GET_ON_LONGITUDE),float(col.GET_ON_LATITUDE)])
#     session.close()
#     return lst

# def query_operate_pos(begin_time_l,geohase5,delta=3600):
#     '''
#     :param begin_time_l:str,like: '2017-02-01 19:0:47'
#     :param geohase7: str
#     :param delta: int
#     :return: [[lon,lat]]
#     '''
#     session = Session()
#     lst = []
#     for col in session.query(Operate).filter(Operate.GEOHASH5 == geohase5).all():
#         if (0<=(get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())<= delta):
#                lst.append([float(col.GET_ON_LONGITUDE),float(col.GET_ON_LATITUDE)])
#     session.close()
#     return lst

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
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 4:
        for col in session.query(OperateRevenue4).filter(OperateRevenue4.CHAUFFEUR_NO == driver_count).filter(OperateRevenue4.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 5:
        for col in session.query(OperateRevenue5).filter(OperateRevenue5.CHAUFFEUR_NO == driver_count).filter(OperateRevenue5.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 6:
        for col in session.query(OperateRevenue6).filter(OperateRevenue6.CHAUFFEUR_NO == driver_count).filter(OperateRevenue6.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 7:
        for col in session.query(OperateRevenue7).filter(OperateRevenue7.CHAUFFEUR_NO == driver_count).filter(OperateRevenue7.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 8:
        for col in session.query(OperateRevenue8).filter(OperateRevenue8.CHAUFFEUR_NO == driver_count).filter(OperateRevenue8.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 9:
        for col in session.query(OperateRevenue9).filter(OperateRevenue9.CHAUFFEUR_NO == driver_count).filter(OperateRevenue9.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 10:
        for col in session.query(OperateRevenue10).filter(OperateRevenue10.CHAUFFEUR_NO == driver_count).filter(OperateRevenue10.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 11:
        for col in session.query(OperateRevenue11).filter(OperateRevenue11.CHAUFFEUR_NO == driver_count).filter(OperateRevenue11.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 12:
        for col in session.query(OperateRevenue12).filter(OperateRevenue12.CHAUFFEUR_NO == driver_count).filter(OperateRevenue12.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 13:
        for col in session.query(OperateRevenue13).filter(OperateRevenue13.CHAUFFEUR_NO == driver_count).filter(OperateRevenue13.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 14:
        for col in session.query(OperateRevenue14).filter(OperateRevenue14.CHAUFFEUR_NO == driver_count).filter(OperateRevenue14.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 15:
        for col in session.query(OperateRevenue15).filter(OperateRevenue15.CHAUFFEUR_NO == driver_count).filter(OperateRevenue15.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 16:
        for col in session.query(OperateRevenue16).filter(OperateRevenue16.CHAUFFEUR_NO == driver_count).filter(OperateRevenue16.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 17:
        for col in session.query(OperateRevenue17).filter(OperateRevenue17.CHAUFFEUR_NO == driver_count).filter(OperateRevenue17.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 18:
        for col in session.query(OperateRevenue18).filter(OperateRevenue18.CHAUFFEUR_NO == driver_count).filter(OperateRevenue18.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 19:
        for col in session.query(OperateRevenue19).filter(OperateRevenue19.CHAUFFEUR_NO == driver_count).filter(OperateRevenue19.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
    elif day == 20:
        for col in session.query(OperateRevenue20).filter(OperateRevenue20.CHAUFFEUR_NO == driver_count).filter(OperateRevenue20.GEOHASH5==geohash).all():
            lst.append([col.EQUIPMENT_ID, float(col.LOAD_MILE), float(col.EMPTY_MILE), col.EMPTY_BEGIN_TIME, col.WORK_BEGIN_TIME, col.WORK_END_TIME, float(col.OPERATE_MONEY)/100])
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
    if day == '2017-02-03':
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
    session.close()
    lst = list(set([tuple(t) for t in lst]))
    all_list = []
    for i in range(len(lst)):
        all_list.append(list(lst[i]))
    return list(all_list)

def income_info(day, geohash, time_):
    session = Session()
    lst = []
    if day == '2017-02-01':
        for col in session.query(OperateRevenue1).filter(OperateRevenue1.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY)/100])

    elif day == '2017-02-02':
        for col in session.query(OperateRevenue2).filter(OperateRevenue2.GEOHASH5 == geohash).all():
            if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                    get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
                lst.append([float(col.OPERATE_MONEY)/100])
    elif day == '2017-02-03':
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
    #input(lst)
    session.close()
    # lst = list(set([tuple(t) for t in lst]))
    # all_list = []
    # for i in range(len(lst)):
    #     all_list.append(list(lst[i]))
    # input(list(all_list))
    # print(lst)
    # input(lst)
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
            lst.extend([float(col.INCOME),[col.BEGIN_TIME,col.END_TIME]])
    session.close()
    return lst

# # 在表中插入数据
# def insert_hot_info(geohash5,period,total_income,empty_mile,show_speed,count):
#     session = Session()
#     print(geohash5,period,total_income,empty_mile,show_speed,count)
#     p = new_table_for_hot(geohash5 = geohash5,period= str(period), total_income=total_income, empty_mile=empty_mile, show_speed=show_speed,count = count)
#     session.add(p)
#     session.commit()
#     session.close()

# 获取所需热点数据
# def get_hot_info(day,geo):
#     session = Session()
#     lst = []
#     if day == '2017-02-01':
#         for geo_ in geo:
#             i = 0
#             one_geo1 = [];one_geo2 = [];one_geo3 = [];one_geo4 = [];one_geo5 = [];one_geo6 = [];one_geo7 = []
#             one_geo8 = [];one_geo9 = [];one_geo10 = [];one_geo11 = [];one_geo12 = [];one_geo13 = [];one_geo14 = []
#             one_geo15 = [];one_geo16 = [];one_geo17 = [];one_geo18 = [];one_geo19 = [];one_geo20 = [];one_geo21 = []
#             one_geo22 = [];one_geo23 = [];one_geo24 = []
#
#             for col in session.query(OperateRevenue1).all():
#                 if  col.GEOHASH5 == geo_:
#                     if int(col.WORK_BEGIN_TIME[11:13]) == 0:
#                         one_geo1.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 1:
#                         one_geo2.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 2:
#                         one_geo3.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 3:
#                         one_geo4.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 4:
#                         one_geo5.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 5:
#                         one_geo6.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 6:
#                         one_geo7.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 7:
#                         one_geo8.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 8:
#                         one_geo9.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 9:
#                         one_geo10.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 10:
#                         one_geo11.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 11:
#                         one_geo12.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 12:
#                         one_geo13.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 13:
#                         one_geo14.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 14:
#                         one_geo15.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 15:
#                         one_geo16.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 16:
#                         one_geo17.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 17:
#                         one_geo18.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 18:
#                         one_geo19.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 19:
#                         one_geo20.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 20:
#                         one_geo21.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 21:
#                         one_geo22.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 22:
#                         one_geo23.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 23:
#                         one_geo24.append([float(col.OPERATE_MONEY)/100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#
#             insert_hot_info(geo_, ['2017-02-01 00:00:00','2017-02-01 01:00:00'], sum([float(i[0]) for i in one_geo1]), sum([float(i[1]) for i in one_geo1]), sum([float(i[2]) for i in one_geo1]),len(one_geo1))
#             insert_hot_info(geo_, ['2017-02-01 01:00:00', '2017-02-01 02:00:00'], sum([float(i[0]) for i in one_geo2]),
#                             sum([float(i[1]) for i in one_geo2]), sum([float(i[2]) for i in one_geo2]), len(one_geo2))
#             insert_hot_info(geo_, ['2017-02-01 02:00:00', '2017-02-01 03:00:00'], sum([float(i[0]) for i in one_geo3]),
#                             sum([float(i[1]) for i in one_geo3]), sum([float(i[2]) for i in one_geo3]), len(one_geo3))
#             insert_hot_info(geo_, ['2017-02-01 03:00:00', '2017-02-01 04:00:00'], sum([float(i[0]) for i in one_geo4]),
#                             sum([float(i[1]) for i in one_geo4]), sum([float(i[2]) for i in one_geo4]), len(one_geo4))
#             insert_hot_info(geo_, ['2017-02-01 04:00:00', '2017-02-01 05:00:00'], sum([float(i[0]) for i in one_geo5]),
#                             sum([float(i[1]) for i in one_geo5]), sum([float(i[2]) for i in one_geo5]), len(one_geo5))
#             insert_hot_info(geo_, ['2017-02-01 05:00:00', '2017-02-01 06:00:00'], sum([float(i[0]) for i in one_geo6]),
#                             sum([float(i[1]) for i in one_geo6]), sum([float(i[2]) for i in one_geo6]), len(one_geo6))
#             insert_hot_info(geo_, ['2017-02-01 06:00:00', '2017-02-01 07:00:00'], sum([float(i[0]) for i in one_geo7]),
#                             sum([float(i[1]) for i in one_geo7]), sum([float(i[2]) for i in one_geo7]), len(one_geo7))
#             insert_hot_info(geo_, ['2017-02-01 07:00:00', '2017-02-01 08:00:00'], sum([float(i[0]) for i in one_geo8]),
#                             sum([float(i[1]) for i in one_geo8]), sum([float(i[2]) for i in one_geo8]), len(one_geo8))
#             insert_hot_info(geo_, ['2017-02-01 08:00:00', '2017-02-01 09:00:00'], sum([float(i[0]) for i in one_geo9]),
#                             sum([float(i[1]) for i in one_geo9]), sum([float(i[2]) for i in one_geo9]), len(one_geo9))
#             insert_hot_info(geo_, ['2017-02-01 09:00:00', '2017-02-01 10:00:00'], sum([float(i[0]) for i in one_geo10]),
#                             sum([float(i[1]) for i in one_geo10]), sum([float(i[2]) for i in one_geo10]), len(one_geo10))
#             insert_hot_info(geo_, ['2017-02-01 10:00:00', '2017-02-01 11:00:00'], sum([float(i[0]) for i in one_geo11]),
#                             sum([float(i[1]) for i in one_geo11]), sum([float(i[2]) for i in one_geo11]), len(one_geo11))
#             insert_hot_info(geo_, ['2017-02-01 11:00:00', '2017-02-01 12:00:00'], sum([float(i[0]) for i in one_geo12]),
#                             sum([float(i[1]) for i in one_geo12]), sum([float(i[2]) for i in one_geo12]), len(one_geo12))
#             insert_hot_info(geo_, ['2017-02-01 12:00:00', '2017-02-01 13:00:00'], sum([float(i[0]) for i in one_geo13]),
#                             sum([float(i[1]) for i in one_geo13]), sum([float(i[2]) for i in one_geo13]), len(one_geo13))
#             insert_hot_info(geo_, ['2017-02-01 13:00:00', '2017-02-01 14:00:00'], sum([float(i[0]) for i in one_geo14]),
#                             sum([float(i[1]) for i in one_geo14]), sum([float(i[2]) for i in one_geo14]), len(one_geo14))
#             insert_hot_info(geo_, ['2017-02-01 14:00:00', '2017-02-01 15:00:00'], sum([float(i[0]) for i in one_geo15]),
#                             sum([float(i[1]) for i in one_geo15]), sum([float(i[2]) for i in one_geo15]), len(one_geo15))
#             insert_hot_info(geo_, ['2017-02-01 15:00:00', '2017-02-01 16:00:00'], sum([float(i[0]) for i in one_geo16]),
#                             sum([float(i[1]) for i in one_geo16]), sum([float(i[2]) for i in one_geo16]), len(one_geo16))
#             insert_hot_info(geo_, ['2017-02-01 16:00:00', '2017-02-01 17:00:00'], sum([float(i[0]) for i in one_geo17]),
#                             sum([float(i[1]) for i in one_geo17]), sum([float(i[2]) for i in one_geo17]), len(one_geo17))
#             insert_hot_info(geo_, ['2017-02-01 17:00:00', '2017-02-01 18:00:00'], sum([float(i[0]) for i in one_geo18]),sum([float(i[1]) for i in one_geo18]), sum([float(i[2]) for i in one_geo18]), len(one_geo18))
#             insert_hot_info(geo_, ['2017-02-01 18:00:00', '2017-02-01 19:00:00'], sum([float(i[0]) for i in one_geo19]),
#                             sum([float(i[1]) for i in one_geo19]), sum([float(i[2]) for i in one_geo19]), len(one_geo19))
#             insert_hot_info(geo_, ['2017-02-01 19:00:00', '2017-02-01 20:00:00'], sum([float(i[0]) for i in one_geo20]),
#                             sum([float(i[1]) for i in one_geo20]), sum([float(i[2]) for i in one_geo20]), len(one_geo20))
#             insert_hot_info(geo_, ['2017-02-01 20:00:00', '2017-02-01 21:00:00'], sum([float(i[0]) for i in one_geo21]),
#                             sum([float(i[1]) for i in one_geo21]), sum([float(i[2]) for i in one_geo21]), len(one_geo21))
#             insert_hot_info(geo_, ['2017-02-01 21:00:00', '2017-02-01 22:00:00'], sum([float(i[0]) for i in one_geo22]),
#                             sum([float(i[1]) for i in one_geo22]), sum([float(i[2]) for i in one_geo22]), len(one_geo22))
#             insert_hot_info(geo_, ['2017-02-01 22:00:00', '2017-02-01 23:00:00'], sum([float(i[0]) for i in one_geo23]),
#                             sum([float(i[1]) for i in one_geo23]), sum([float(i[2]) for i in one_geo23]), len(one_geo23))
#             insert_hot_info(geo_, ['2017-02-01 23:00:00', '2017-02-01 24:00:00'], sum([float(i[0]) for i in one_geo13]),
#                             sum([float(i[1]) for i in one_geo24]), sum([float(i[2]) for i in one_geo24]), len(one_geo24))
#
#     elif day == '2017-02-02':
#         for col in session.query(OperateRevenue2).filter(OperateRevenue2.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-03':
#         for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-04':
#         for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-05':
#         for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-06':
#         for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-07':
#         for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-08':
#         for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-09':
#         for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-10':
#         for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-11':
#         for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     elif day == '2017-02-12':
#         for geo_ in geo:
#             one_geo1 = [];one_geo2 = [];one_geo3 = [];one_geo4 = [];one_geo5 = [];one_geo6 = [];one_geo7 = []
#             one_geo8 = [];one_geo9 = [];one_geo10 = [];one_geo11 = [];one_geo12 = [];one_geo13 = [];one_geo14 = []
#             one_geo15 = [];one_geo16 = [];one_geo17 = [];one_geo18 = [];one_geo19 = [];one_geo20 = [];one_geo21 = []
#             one_geo22 = [];one_geo23 = [];one_geo24 = []
#
#             for col in session.query(OperateRevenue1).all():
#                 if col.GEOHASH5 == geo_:
#                     if int(col.WORK_BEGIN_TIME[11:13]) == 0:
#                         one_geo1.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 1:
#                         one_geo2.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 2:
#                         one_geo3.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 3:
#                         one_geo4.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 4:
#                         one_geo5.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 5:
#                         one_geo6.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 6:
#                         one_geo7.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 7:
#                         one_geo8.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 8:
#                         one_geo9.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 9:
#                         one_geo10.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 10:
#                         one_geo11.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 11:
#                         one_geo12.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 12:
#                         one_geo13.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 13:
#                         one_geo14.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 14:
#                         one_geo15.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 15:
#                         one_geo16.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 16:
#                         one_geo17.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 17:
#                         one_geo18.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 18:
#                         one_geo19.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 19:
#                         one_geo20.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 20:
#                         one_geo21.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 21:
#                         one_geo22.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 22:
#                         one_geo23.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#                     elif int(col.WORK_BEGIN_TIME[11:13]) == 23:
#                         one_geo24.append([float(col.OPERATE_MONEY) / 100, col.EMPTY_MILE, col.SLOW_COUNT_TIME])
#
#             insert_hot_info(geo_, ['2017-02-12 00:00:00', '2017-02-12 01:00:00'], sum([float(i[0]) for i in one_geo1]),
#                             sum([float(i[1]) for i in one_geo1]), sum([float(i[2]) for i in one_geo1]), len(one_geo1))
#             insert_hot_info(geo_, ['2017-02-12 01:00:00', '2017-02-12 02:00:00'], sum([float(i[0]) for i in one_geo2]),
#                             sum([float(i[1]) for i in one_geo2]), sum([float(i[2]) for i in one_geo2]), len(one_geo2))
#             insert_hot_info(geo_, ['2017-02-12 02:00:00', '2017-02-12 03:00:00'], sum([float(i[0]) for i in one_geo3]),
#                             sum([float(i[1]) for i in one_geo3]), sum([float(i[2]) for i in one_geo3]), len(one_geo3))
#             insert_hot_info(geo_, ['2017-02-12 03:00:00', '2017-02-12 04:00:00'], sum([float(i[0]) for i in one_geo4]),
#                             sum([float(i[1]) for i in one_geo4]), sum([float(i[2]) for i in one_geo4]), len(one_geo4))
#             insert_hot_info(geo_, ['2017-02-12 04:00:00', '2017-02-12 05:00:00'], sum([float(i[0]) for i in one_geo5]),
#                             sum([float(i[1]) for i in one_geo5]), sum([float(i[2]) for i in one_geo5]), len(one_geo5))
#             insert_hot_info(geo_, ['2017-02-12 05:00:00', '2017-02-12 06:00:00'], sum([float(i[0]) for i in one_geo6]),
#                             sum([float(i[1]) for i in one_geo6]), sum([float(i[2]) for i in one_geo6]), len(one_geo6))
#             insert_hot_info(geo_, ['2017-02-12 06:00:00', '2017-02-12 07:00:00'], sum([float(i[0]) for i in one_geo7]),
#                             sum([float(i[1]) for i in one_geo7]), sum([float(i[2]) for i in one_geo7]), len(one_geo7))
#             insert_hot_info(geo_, ['2017-02-12 07:00:00', '2017-02-12 08:00:00'], sum([float(i[0]) for i in one_geo8]),
#                             sum([float(i[1]) for i in one_geo8]), sum([float(i[2]) for i in one_geo8]), len(one_geo8))
#             insert_hot_info(geo_, ['2017-02-12 08:00:00', '2017-02-12 09:00:00'], sum([float(i[0]) for i in one_geo9]),
#                             sum([float(i[1]) for i in one_geo9]), sum([float(i[2]) for i in one_geo9]), len(one_geo9))
#             insert_hot_info(geo_, ['2017-02-12 09:00:00', '2017-02-12 10:00:00'], sum([float(i[0]) for i in one_geo10]),
#                             sum([float(i[1]) for i in one_geo10]), sum([float(i[2]) for i in one_geo10]),
#                             len(one_geo10))
#             insert_hot_info(geo_, ['2017-02-12 10:00:00', '2017-02-12 11:00:00'], sum([float(i[0]) for i in one_geo11]),
#                             sum([float(i[1]) for i in one_geo11]), sum([float(i[2]) for i in one_geo11]),
#                             len(one_geo11))
#             insert_hot_info(geo_, ['2017-02-12 11:00:00', '2017-02-12 12:00:00'], sum([float(i[0]) for i in one_geo12]),
#                             sum([float(i[1]) for i in one_geo12]), sum([float(i[2]) for i in one_geo12]),
#                             len(one_geo12))
#             insert_hot_info(geo_, ['2017-02-12 12:00:00', '2017-02-12 13:00:00'], sum([float(i[0]) for i in one_geo13]),
#                             sum([float(i[1]) for i in one_geo13]), sum([float(i[2]) for i in one_geo13]),
#                             len(one_geo13))
#             insert_hot_info(geo_, ['2017-02-12 13:00:00', '2017-02-12 14:00:00'], sum([float(i[0]) for i in one_geo14]),
#                             sum([float(i[1]) for i in one_geo14]), sum([float(i[2]) for i in one_geo14]),
#                             len(one_geo14))
#             insert_hot_info(geo_, ['2017-02-12 14:00:00', '2017-02-12 15:00:00'], sum([float(i[0]) for i in one_geo15]),
#                             sum([float(i[1]) for i in one_geo15]), sum([float(i[2]) for i in one_geo15]),
#                             len(one_geo15))
#             insert_hot_info(geo_, ['2017-02-12 15:00:00', '2017-02-12 16:00:00'], sum([float(i[0]) for i in one_geo16]),
#                             sum([float(i[1]) for i in one_geo16]), sum([float(i[2]) for i in one_geo16]),
#                             len(one_geo16))
#             insert_hot_info(geo_, ['2017-02-12 16:00:00', '2017-02-12 17:00:00'], sum([float(i[0]) for i in one_geo17]),
#                             sum([float(i[1]) for i in one_geo17]), sum([float(i[2]) for i in one_geo17]),
#                             len(one_geo17))
#             insert_hot_info(geo_, ['2017-02-12 17:00:00', '2017-02-12 18:00:00'], sum([float(i[0]) for i in one_geo18]),
#                             sum([float(i[1]) for i in one_geo18]), sum([float(i[2]) for i in one_geo18]),
#                             len(one_geo18))
#             insert_hot_info(geo_, ['2017-02-12 18:00:00', '2017-02-12 19:00:00'], sum([float(i[0]) for i in one_geo19]),
#                             sum([float(i[1]) for i in one_geo19]), sum([float(i[2]) for i in one_geo19]),
#                             len(one_geo19))
#             insert_hot_info(geo_, ['2017-02-12 19:00:00', '2017-02-12 20:00:00'], sum([float(i[0]) for i in one_geo20]),
#                             sum([float(i[1]) for i in one_geo20]), sum([float(i[2]) for i in one_geo20]),
#                             len(one_geo20))
#             insert_hot_info(geo_, ['2017-02-12 20:00:00', '2017-02-12 21:00:00'], sum([float(i[0]) for i in one_geo21]),
#                             sum([float(i[1]) for i in one_geo21]), sum([float(i[2]) for i in one_geo21]),
#                             len(one_geo21))
#             insert_hot_info(geo_, ['2017-02-12 21:00:00', '2017-02-12 22:00:00'], sum([float(i[0]) for i in one_geo22]),
#                             sum([float(i[1]) for i in one_geo22]), sum([float(i[2]) for i in one_geo22]),
#                             len(one_geo22))
#             insert_hot_info(geo_, ['2017-02-12 22:00:00', '2017-02-12 23:00:00'], sum([float(i[0]) for i in one_geo23]),
#                             sum([float(i[1]) for i in one_geo23]), sum([float(i[2]) for i in one_geo23]),
#                             len(one_geo23))
#             insert_hot_info(geo_, ['2017-02-12 23:00:00', '2017-02-12 24:00:00'], sum([float(i[0]) for i in one_geo13]),
#                             sum([float(i[1]) for i in one_geo24]), sum([float(i[2]) for i in one_geo24]),
#                             len(one_geo24))
#         print("1")
#     elif day == '2017-02-13':
#         for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-14':
#         for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-15':
#         for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-16':
#         for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-17':
#         for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-18':
#         for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-19':
#         for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-20':
#         for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#
#     elif day == '2017-02-21':
#         for col in session.query(OperateRevenue21).filter(OperateRevenue21.GEOHASH5 == geohash).all():
#             if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
#                     get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
#                 lst.append([float(col.OPERATE_MONEY) / 100])
#     session.close()
#     return list(lst)

# 有用的函数

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
    # with open('lst.py','w') as f:
    #     f.write(str(lst))