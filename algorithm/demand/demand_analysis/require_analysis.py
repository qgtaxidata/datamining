
import mzgeohash
import warnings
from db_tools import *
warnings.filterwarnings('ignore')

"""
需求分析函数：
输入参数：（geohash，time）
geohash编码为七位编码
time为时间
返回：两个字典：一，相关与需求量：n为北，ne为东北，e为东
  二，收入数据
"""

def find_mysql(geohash_, time):
    """利用geohash编码找到对应区块的订单信息"""
    all_points = query_operate_price(time, geohash_)
    return all_points
    # 根据geohash、time 找到对应的单子，返回二维列表

def demand_analysis(geohash,time):
    neighbor = mzgeohash.neighbors(geohash)
    order_dict = {}
    income_dict = {}
    for key in neighbor.keys():
        geohash = neighbor[key]
        datas = find_mysql(geohash, time)
        order_count = len(datas)
        income = sum([data for data in datas])
        order_dict[key] = order_count
        income_dict[key] = income
    return order_dict, income_dict

order_dict, income_dict = demand_analysis('ws0e9kx', '2017-02-03 17:30:02')
print('需求订单:',order_dict)
print('收入数据:',income_dict)