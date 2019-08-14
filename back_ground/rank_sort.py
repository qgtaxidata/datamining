# -*- coding:utf-8 -*-

from db_tools import *
import warnings
import json
warnings.filterwarnings('ignore')

def get_rank(area_dict):
    area = area_dict['area']
    date = str(int(area_dict['date'][-2:]))
    ranking = get_operate_rank(area, date)[0]
    print(len(ranking))
    rank = 1
    rank_list = []
    for key in ranking.keys():
        driver_rank = {}
        driver_rank['rank'] = rank
        driver_rank['driverID'] = key
        driver_rank['income'] = ranking[key]
        rank_list.append(driver_rank)
        rank += 1
    if len(rank_list) > 20:
        rank_list = rank_list[:20]
    return rank_list

if __name__ == '__main__':
    area_dict = {'area': 4, 'date': '2017-02-03'}
    get_rank(area_dict)