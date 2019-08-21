# -*- coding:utf-8 -*-
from db_tools.base_table import *
from datetime import datetime

def get_date_time(strs):
    return datetime.strptime(strs,'%Y-%m-%d %H:%M:%S')

# def query_operate_pos(begin_time_l,geohase7,delta=30):
#     '''
#     :param begin_time_l:str,like: '2017-02-01 19:0:47'
#     :param geohase7: str
#     :param delta: int
#     :return: [[lon,lat]]
#     '''
#     session = Session()
#     lst = []
#     for col in session.query(Operate).filter(Operate.GEOHASH5 == geohase7).all():
#         if (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta:
#             lst.append([float(col.GET_ON_LONGITUDE),float(col.GET_ON_LATITUDE)])
#     session.close()
#     return lst
# 函数更新如下：
def query_operate_pos(begin_time_l,geohase5,delta=3600):
    '''
    :param begin_time_l:str,like: '2017-02-01 19:0:47'
    :param geohase7: str
    :param delta: int
    :return: [[lon,lat]]
    '''
    session = Session()
    lst = []
    for col in session.query(Operate).filter(Operate.GEOHASH5 == geohase5).all():
        if (0<=(get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())<= delta):
               lst.append([float(col.GET_ON_LONGITUDE),float(col.GET_ON_LATITUDE)])
    session.close()
    return lst


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

#这部分代码属于收入排行榜使用的算法，故可以注释
# def get_operate_his(day):
#     session = Session()
#     lst = []
#     if day == 3:
#         for col in session.query(OperateRevenue3).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 4:
#         for col in session.query(OperateRevenue4).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 5:
#         for col in session.query(OperateRevenue5).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 6:
#         for col in session.query(OperateRevenue6).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 7:
#         for col in session.query(OperateRevenue7).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 8:
#         for col in session.query(OperateRevenue8).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 9:
#         for col in session.query(OperateRevenue9).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 10:
#         for col in session.query(OperateRevenue10).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 11:
#         for col in session.query(OperateRevenue11).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 12:
#         for col in session.query(OperateRevenue12).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 13:
#         for col in session.query(OperateRevenue13).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 14:
#         for col in session.query(OperateRevenue14).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 15:
#         for col in session.query(OperateRevenue15).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 16:
#         for col in session.query(OperateRevenue16).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 17:
#         for col in session.query(OperateRevenue17).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 18:
#         for col in session.query(OperateRevenue18).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 19:
#         for col in session.query(OperateRevenue19).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 20:
#         for col in session.query(OperateRevenue20).all():
#             lst.append(col.CHAUFFEUR_NO)
#     session.close()
#     return list(set(lst))
#
# def get_operate_revenue(drive, geohash, day):
#     session = Session()
#     lst = []
#     if day == 3:
#         for col in session.query(OperateRevenue3).filter(OperateRevenue3.CHAUFFEUR_NO == drive).filter(OperateRevenue3.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 4:
#         for col in session.query(OperateRevenue4).filter(OperateRevenue4.CHAUFFEUR_NO == drive).filter(OperateRevenue4.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 5:
#         for col in session.query(OperateRevenue5).filter(OperateRevenue5.CHAUFFEUR_NO == drive).filter(OperateRevenue5.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 6:
#         for col in session.query(OperateRevenue6).filter(OperateRevenue6.CHAUFFEUR_NO == drive).filter(OperateRevenue6.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 7:
#         for col in session.query(OperateRevenue7).filter(OperateRevenue7.CHAUFFEUR_NO == drive).filter(OperateRevenue7.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 8:
#         for col in session.query(OperateRevenue8).filter(OperateRevenue8.CHAUFFEUR_NO == drive).filter(OperateRevenue8.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 9:
#         for col in session.query(OperateRevenue9).filter(OperateRevenue9.CHAUFFEUR_NO == drive).filter(OperateRevenue9.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 10:
#         for col in session.query(OperateRevenue10).filter(OperateRevenue10.CHAUFFEUR_NO == drive).filter(OperateRevenue10.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 11:
#         for col in session.query(OperateRevenue11).filter(OperateRevenue11.CHAUFFEUR_NO == drive).filter(OperateRevenue11.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 12:
#         for col in session.query(OperateRevenue12).filter(OperateRevenue12.CHAUFFEUR_NO == drive).filter(OperateRevenue12.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 13:
#         for col in session.query(OperateRevenue13).filter(OperateRevenue13.CHAUFFEUR_NO == drive).filter(OperateRevenue13.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 14:
#         for col in session.query(OperateRevenue14).filter(OperateRevenue14.CHAUFFEUR_NO == drive).filter(OperateRevenue14.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 15:
#         for col in session.query(OperateRevenue15).filter(OperateRevenue15.CHAUFFEUR_NO == drive).filter(OperateRevenue15.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 16:
#         for col in session.query(OperateRevenue16).filter(OperateRevenue16.CHAUFFEUR_NO == drive).filter(OperateRevenue16.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 17:
#         for col in session.query(OperateRevenue17).filter(OperateRevenue17.CHAUFFEUR_NO == drive).filter(OperateRevenue17.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
#     elif day == 18:
#         for col in session.query(OperateRevenue18).filter(OperateRevenue18.CHAUFFEUR_NO == drive).filter(OperateRevenue18.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 19:
#         for col in session.query(OperateRevenue19).filter(OperateRevenue19.CHAUFFEUR_NO == drive).filter(OperateRevenue19.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     elif day == 20:
#         for col in session.query(OperateRevenue20).filter(OperateRevenue20.CHAUFFEUR_NO == drive).filter(OperateRevenue20.GEOHASH5 == geohash).all():
#             lst.append([col.WORK_BEGIN_TIME, float(col.OPERATE_MONEY) / 100])
#     session.close()
#     lst = list(set([tuple(t) for t in lst]))
#     all_list = []
#     for i in range(len(lst)):
#         all_list.append(lst[i][1])
#     return list(all_list)
#
# def get_drive_operste(geohash, day):
#     session = Session()
#     lst = []
#     if day == 3:
#         for col in session.query(OperateRevenue3).filter(OperateRevenue3.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 4:
#         for col in session.query(OperateRevenue4).filter(OperateRevenue4.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 5:
#         for col in session.query(OperateRevenue5).filter(OperateRevenue5.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 6:
#         for col in session.query(OperateRevenue6).filter(OperateRevenue6.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 7:
#         for col in session.query(OperateRevenue7).filter(OperateRevenue7.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 8:
#         for col in session.query(OperateRevenue8).filter(OperateRevenue8.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 9:
#         for col in session.query(OperateRevenue9).filter(OperateRevenue9.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 10:
#         for col in session.query(OperateRevenue10).filter(OperateRevenue10.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 11:
#         for col in session.query(OperateRevenue11).filter(OperateRevenue11.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 12:
#         for col in session.query(OperateRevenue12).filter(OperateRevenue12.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 13:
#         for col in session.query(OperateRevenue13).filter(OperateRevenue13.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 14:
#         for col in session.query(OperateRevenue14).filter(OperateRevenue14.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 15:
#         for col in session.query(OperateRevenue15).filter(OperateRevenue15.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 16:
#         for col in session.query(OperateRevenue16).filter(OperateRevenue16.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 17:
#         for col in session.query(OperateRevenue17).filter(OperateRevenue17.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 18:
#         for col in session.query(OperateRevenue18).filter(OperateRevenue18.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 19:
#         for col in session.query(OperateRevenue19).filter(OperateRevenue19.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     elif day == 20:
#         for col in session.query(OperateRevenue20).filter(OperateRevenue20.GEOHASH5 == geohash).all():
#             lst.append(col.CHAUFFEUR_NO)
#     session.close()
#     lst = list(set(lst))
#     return lst

# # 收入预测之用
# def get_operate_order(geo_):
#     session = Session()
#     total_order = []
#     d0 = [];d1 = [];d2 = [];d3 = [];d4 = [];d5 = [];d6 = [];d7 = [];d8 = [];d9 = [];d10 = []
#     for col in session.query(OperateRevenue3).all():
#         if col.GEOHASH5 in geo_[0]:
#             d0.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[1]:
#             d1.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[2]:
#             d2.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[3]:
#             d3.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[4]:
#             d4.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[5]:
#             d5.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[6]:
#             d6.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[7]:
#             d7.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[8]:
#             d8.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[9]:
#             d9.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE,col.SLOW_COUNT_TIME,col.UNIT_PRICE,col.OPERATE_MONEY])
#         if col.GEOHASH5 in geo_[10]:
#             d10.append([col.CHAUFFEUR_NO, col.LOAD_MILE, col.EMPTY_MILE, col.SLOW_COUNT_TIME, col.UNIT_PRICE,col.OPERATE_MONEY])
#     total_order.append(d0)
#     total_order.append(d1)
#     total_order.append(d2)
#     total_order.append(d3)
#     total_order.append(d4)
#     total_order.append(d5)
#     total_order.append(d6)
#     total_order.append(d7)
#     total_order.append(d8)
#     total_order.append(d9)
#     total_order.append(d10)
#     session.close()
#     # input(total_order[0])
#     return total_order

def insert_operate_ranking(day, Admin, ranking):
    session = Session()
    p = OperateRevenueRanking(day=day, Admin=Admin, ranking=ranking)
    session.add(p)
    session.commit()
    session.close()

if __name__ =='__main__':
    geohase7='ws0e9u4'
    begin_time_l ='2017-02-01 0:0:0'
    begin_time_u = '2017-02-02 19:53:47'
    # lst = query_operate(begin_time_l,geohase7)
    # lst = query_operate_(begin_time_l,begin_time_u,None)
