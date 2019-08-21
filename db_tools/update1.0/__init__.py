#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base_table as *
from datetime import datetime,timedelta

def get_date_time(strs):
    return datetime.strptime(strs,'%Y-%m-%d %H:%M:%S')


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
    table_dataset = {'2017-02-01':OperateRevenue1,'2017-02-02':OperateRevenue2,'2017-02-03':OperateRevenue3,'2017-02-04':OperateRevenue4,'2017-02-05':OperateRevenue5,'2017-02-06':OperateRevenue6,'2017-02-07':OperateRevenue7,'2017-02-08':OperateRevenue8,'2017-02-09':OperateRevenue9,'2017-02-10':OperateRevenue10,'2017-02-11':OperateRevenue11,'2017-02-12':OperateRevenue12,'2017-02-13':OperateRevenue13,'2017-02-14':OperateRevenue14,'2017-02-15':OperateRevenue15,'2017-02-16':OperateRevenue16,'2017-02-17':OperateRevenue17,'2017-02-18':OperateRevenue18,'2017-02-19':OperateRevenue19,'2017-02-20':OperateRevenue20,'2017-02-21':OperateRevenue21}
    
    for col in session.query(table_dataset[day]).filter(table_dataset[day].GEOHASH5 == geohase5).all():
        if (0 <= (get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp())) & ((get_date_time(begin_time_l).timestamp() - get_date_time(col.WORK_BEGIN_TIME).timestamp()) <= delta):
            lst.append([float(col.GET_ON_LONGITUDE), float(col.GET_ON_LATITUDE)]
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
    table_dataset = {1:OperateRevenue1,2:OperateRevenue2,3:OperateRevenue3,4:OperateRevenue4,5:OperateRevenue5,6:OperateRevenue6,7:OperateRevenue7,8:OperateRevenue8,9:OperateRevenue9,10:OperateRevenue10,11:OperateRevenue11,12:OperateRevenue12,13:OperateRevenue13,14:OperateRevenue14,15:OperateRevenue15,16:OperateRevenue16,17:OperateRevenue17,18:OperateRevenue18,19:OperateRevenue19,20:OperateRevenue20,21:OperateRevenue21}
    for col in session.query(table_dataset[day]).all():
        lst.append(col.CHAUFFEUR_NO)
    session.close()
    return list(set(lst))

def get_operate_revenue(drive, geohash, day):
    session = Session()
    lst = []
    table_dataset = {1:OperateRevenue1,2:OperateRevenue2,3:OperateRevenue3,4:OperateRevenue4,5:OperateRevenue5,6:OperateRevenue6,7:OperateRevenue7,8:OperateRevenue8,9:OperateRevenue9,10:OperateRevenue10,11:OperateRevenue11,12:OperateRevenue12,13:OperateRevenue13,14:OperateRevenue14,15:OperateRevenue15,16:OperateRevenue16,17:OperateRevenue17,18:OperateRevenue18,19:OperateRevenue19,20:OperateRevenue20,21:OperateRevenue21}
    for col in session.query(table_dataset[day]).filter(table_dataset[day].CHAUFFEUR_NO == drive).filter(table_dataset[day].GEOHASH5 == geohash).all():
            lst.append([col.WORK_BEGIN_TIME,float(col.OPERATE_MONEY)/100])
    session.close()
    lst = list(set([tuple(t) for t in lst]))
    all_list = []
    for i in range(len(lst)):
        all_list.append(lst[i][1])
    return list(all_list)

def get_drive_operste(geohash, day):
    session = Session()
    lst = []
    table_dataset = {1:OperateRevenue1,2:OperateRevenue2,3:OperateRevenue3,4:OperateRevenue4,5:OperateRevenue5,6:OperateRevenue6,7:OperateRevenue7,8:OperateRevenue8,9:OperateRevenue9,10:OperateRevenue10,11:OperateRevenue11,12:OperateRevenue12,13:OperateRevenue13,14:OperateRevenue14,15:OperateRevenue15,16:OperateRevenue16,17:OperateRevenue17,18:OperateRevenue18,19:OperateRevenue19,20:OperateRevenue20,21:OperateRevenue21}
    for col in session.query(table_dataset[day]).filter(table_dataset[day].GEOHASH5==geohash).all():
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
    table_dataset = {1:OperateRevenue1,2:OperateRevenue2,3:OperateRevenue3,4:OperateRevenue4,5:OperateRevenue5,6:OperateRevenue6,7:OperateRevenue7,8:OperateRevenue8,9:OperateRevenue9,10:OperateRevenue10,11:OperateRevenue11,12:OperateRevenue12,13:OperateRevenue13,14:OperateRevenue14,15:OperateRevenue15,16:OperateRevenue16,17:OperateRevenue17,18:OperateRevenue18,19:OperateRevenue19,20:OperateRevenue20,21:OperateRevenue21}
    for col in session.query(table_dataset[day]).filter(table_dataset[day].CHAUFFEUR_NO == driver_count).filter(table_dataset[day].GEOHASH5==geohash).all():
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
    table_dataset = {'2017-02-01':OperateRevenue1,'2017-02-02':OperateRevenue2,'2017-02-03':OperateRevenue3,'2017-02-04':OperateRevenue4,'2017-02-05':OperateRevenue5,'2017-02-06':OperateRevenue6,'2017-02-07':OperateRevenue7,'2017-02-08':OperateRevenue8,'2017-02-09':OperateRevenue9,'2017-02-10':OperateRevenue10,'2017-02-11':OperateRevenue11,'2017-02-12':OperateRevenue12,'2017-02-13':OperateRevenue13,'2017-02-14':OperateRevenue14,'2017-02-15':OperateRevenue15,'2017-02-16':OperateRevenue16,'2017-02-17':OperateRevenue17,'2017-02-18':OperateRevenue18,'2017-02-19':OperateRevenue19,'2017-02-20':OperateRevenue20,'2017-02-21':OperateRevenue21}
    for col in session.query(table_dataset[day]).filter(table_dataset[day].GEOHASH5==geohash).all():
        if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
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
    table_dataset = {'2017-02-01':OperateRevenue1,'2017-02-02':OperateRevenue2,'2017-02-03':OperateRevenue3,'2017-02-04':OperateRevenue4,'2017-02-05':OperateRevenue5,'2017-02-06':OperateRevenue6,'2017-02-07':OperateRevenue7,'2017-02-08':OperateRevenue8,'2017-02-09':OperateRevenue9,'2017-02-10':OperateRevenue10,'2017-02-11':OperateRevenue11,'2017-02-12':OperateRevenue12,'2017-02-13':OperateRevenue13,'2017-02-14':OperateRevenue14,'2017-02-15':OperateRevenue15,'2017-02-16':OperateRevenue16,'2017-02-17':OperateRevenue17,'2017-02-18':OperateRevenue18,'2017-02-19':OperateRevenue19,'2017-02-20':OperateRevenue20,'2017-02-21':OperateRevenue21}
    for col in session.query(table_dataset[day]).filter(table_dataset[day].GEOHASH5==geohash).all():
        if (get_date_time(col.EMPTY_BEGIN_TIME) > get_date_time(time_[0])) and (
                get_date_time(col.EMPTY_BEGIN_TIME) <= get_date_time(time_[1])):
            lst.append([float(col.OPERATE_MONEY)/100])
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
            lst.extend([float(col.INCOME),[col.BEGIN_TIME,col.END_TIME]])
    session.close()
    return lst


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
                       
    table_dataset = {'2017-02-01':OperateRevenue1,'2017-02-02':OperateRevenue2,'2017-02-03':OperateRevenue3,'2017-02-04':OperateRevenue4,'2017-02-05':OperateRevenue5,'2017-02-06':OperateRevenue6,'2017-02-07':OperateRevenue7,'2017-02-08':OperateRevenue8,'2017-02-09':OperateRevenue9,'2017-02-10':OperateRevenue10,'2017-02-11':OperateRevenue11,'2017-02-12':OperateRevenue12,'2017-02-13':OperateRevenue13,'2017-02-14':OperateRevenue14,'2017-02-15':OperateRevenue15,'2017-02-16':OperateRevenue16,'2017-02-17':OperateRevenue17,'2017-02-18':OperateRevenue18,'2017-02-19':OperateRevenue19,'2017-02-20':OperateRevenue20,'2017-02-21':OperateRevenue21}
    for col in session.query(table_dataset[day]).all():
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

