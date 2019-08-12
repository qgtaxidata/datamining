from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import warnings
import random
import datetime
import numpy as np
from geo_hash_paint import get_geolonlat
warnings.filterwarnings('ignore')
from taxi_bigdata.db_tools import *
from line_return import *

"""
输入的json格式 = [[最前一段时间],[前一段时间],[实时时间]]
如：json = [[{"lng":116.191031,"lat":39.988585,"count":12}, {"lng":116.191031,"lat":39.988585,"count":14}, {"lng":116.191031,"lat":39.988585,"count":12}],[{"lng":116.191031,"lat":39.988585,"count":10}, {"lng":116.191031,"lat":39.988585,"count":14}, {"lng":116.191031,"lat":39.988585,"count":8}],[{"lng":116.191031,"lat":39.988585,"count":16}, {"lng":116.191031,"lat":39.988585,"count":5}, {"lng":116.191031,"lat":39.988585,"count":6}]]
调用：hot_line(json) 线性回归模型
      hot_GaussianNB  高斯回归模型
      hot_hot_MultinomialNB  多项式模型
      hot_BernoulliNB  伯努利模型
返回： now_hot = [{"lng":116.191031,"lat":39.988585,"count":12}, {"lng":116.191031,"lat":39.988585,"count":14}, {"lng":116.191031,"lat":39.988585,"count":12}]
       counts  总个数 
"""

#四个预测算法
def line_predict(X, y, x_predict):
    """线性预测"""
    model = linear_model.LinearRegression()
    model.fit(X, y)
    print(model.intercept_)  # 截距
    print(model.coef_)  # 线性模型的系数
    a = x_predict*model.coef_[0] + model.intercept_[0]
    result = model.predict(x_predict)
    return result
#四个预测模型套用
def hot_line(all_lists):
    post_hot1 = all_lists[0]
    post_hot2 = all_lists[1]
    now_hot = all_lists[2]
    predict_hots = []
    counts = 0
    for i in range(len(post_hot1)):
        X = [[1], [2], [3]];y = [];predict_hot = {}
        y.append([post_hot1[i]['count']])
        y.append([post_hot2[i]['count']])
        y.append([now_hot[i]['count']])
        x_predict = [[4]]
        result = line_predict(X, y, x_predict)
        predict_hot['lng'] = post_hot1[i]['lng']
        predict_hot['lat'] = post_hot1[i]['lat']
        predict_hot['count'] = int(result[0][0])
        predict_hots.append(predict_hot)
        counts += int(result[0][0])
    return predict_hots, counts
def train_ridge(X, y):
    model = linear_model.Ridge
    model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
    model.fit(X, y)
    return [model.intercept_[0], model.coef_[0][0]]  # 截距，系数
def train_line(X,y):
    model = linear_model.LinearRegression()
    model.fit(X, y)
    return [model.intercept_[0], model.coef_[0][0]]  #截距，系数

def train_parameter():
    guangzhou_geohash5 = list(set(query_operate_geohash()))
    # guangzhou_geohash5 = ['ws08b', 'ws0s8', 'ws0sh', 'ws0ed', 'ws0s4', 'ws0d9', 'ws07y', 'ws0tm', 'ws0s9', 'ws0v1', 'ws0gq', 'ws0dd', 'w7z5b', 'ws0s1', 'ws0ep', 'ws0d6', 'ws0sf', 'ws0ew', 'ws0sb', 'ws0ef', 'ws0sq', 'ws0df', 'ws0es', 'ws0e6', 'ws0mp', 'ws072', 'ws071', 'ws0e2', 'ws09m', 'ws0sn', 'ws0t0', 'ws0ec', 'ws0t1', 'ws0dt', 'ws0sw', 'w7ys2', 'ws0t4', 'ws079', 'ws09f', 'ws09x', 'ws0dg', 'ws0ey', 'ws0w4', 'ws0kc', 'ws0kp', 'ws07p', 'ws0du', 'ws0dj', 'ws0wv', 'ws0de', 'ws0g5', 'ws09c', 'ws0s6', 'ws0g2', 'ws0s5', 'ws0e9', 'ws0th', 'ws07x', 'ws07t', 'ws0ut', 'ws0t2', 'ws0sc', 'ws07n', 'ws0s7', 'ws0sj', 'ws0yd', 'wms6w', 'ws0s3', 'ws0ev', 'ws0y0', 'ws09w', 'ws0kn', 'ws07z', 'ws0eu', 'ws09z', 'ws0et', 'ws0eh', 'ws0en', 'ws0d0', 'ws0tj', 'ws07j', 'ws0fu', 'ws0bc', 'ws0e4', 'ws30y', 'ws0dk', 'ws07w', 'ws0e1', 'ws222', 'ws0e7', 'ws0eq', 'ws0me', 'ws0w8', 'ws0db', 'ws0sz', 'ws0um', 'ws0ex', 'ws0k7', 'ws07q', 'ws0d3', 'ws0tq', 'w7yw1', 'ws0e0', 'ws0em', 'ws0sg', 'wt2bv', 'ws0dc', 'ws0cb', 'ws0mr', 'ws0e8', 'ws146', 'ws0g8', 'ws0t6', 'webx7', 'webwr', 'ws0g9', 'ws0tw', 'ws0su', 'ws0gb', 'ws0gk', 'ws0e5', 'ws0st', 'ws0t9', 'ws0u2']
    time = '2017-02-01 23:55:00'
    add_time = 0
    # X = [[5], [10], [15], [20], [25], [30]]
    times = list(range(0, 1440, 5))
    X = []; X_more=[]
    num = 0
    for x in times :
        X.append([x])
        X_more.append(x)
    for geohash in guangzhou_geohash5:
        y = [];y_more=[]
        for i in range(1, len(X) + 1):
            order_price = query_operate_price_del(time, geohash, i)
            if order_price == []:
                y.append([0])
                y_more.append(0)
            elif order_price != []:
                y.append([len(order_price)])
                y_more.append(len(order_price))
        # y = np.concatenate(y, axis=0)
        line_more_parameter = line_more_train(X_more, y_more)
        line_parameter = train_line(X, y)
        Ridge_paramter = train_ridge(X, y)
        print(line_parameter, Ridge_paramter, line_more_parameter, num)
        num += 1
        insert_operate_params(geohash, str(line_parameter), str(line_more_parameter), str(Ridge_paramter))

def line_more_train(X, y):
    X = np.array(X)
    y = np.array(y)
    f1 = list(np.polyfit(X, y, 10))
    return f1

def line_more_model(line_pareter, time):
    sum = 0
    for i in range(len(line_pareter)):
        sum += line_pareter[i]*time
    return sum

def linear_models(line_paramter, time):
    return line_paramter[0]*time + line_paramter[1]

def GaussianNB_model(GaussianNB_parameter, time):
    sigma = np.mat(GaussianNB_parameter[1])
    u = np.mat(GaussianNB_parameter[0])
    time = np.mat(time)
    outxishu = 1 / (np.sqrt(2 * np.pi * sigma))
    inxishu = -((time - u) ** 2) / (2 * sigma)
    return outxishu * np.exp(inxishu)  # 高斯公式


def get_hotpredict(geohash, time):
    parameter = get_operate_params(geohash)[0]
    line_parameter = eval(parameter[0])
    Ridge_paramter = eval(parameter[2])
    daytime = time[-8:]
    time = float(daytime[:2])*60.0 + float(daytime[3:5]) + float(daytime[-2:])/60.0
    line_result = int(linear_models(line_parameter, time))


if __name__ == '__main__':
    train_parameter()
    # insert_operate_params('123', 'q23', '12', '123')
    # get_hotpredict('ws07h', '2017-02-01 20:09:40')













    # predict_hots, counts = hot_line(json)
    # predict_hots1, counts1 = hot_GaussianNB(json)
    # predict_hots2, counts2 = hot_MultinomialNB(json)
    # predict_hots3, counts3 = hot_BernoulliNB(json)
    # print(predict_hots, counts)
    # print(predict_hots1, counts1)
    # print(predict_hots2, counts2)
    # print(predict_hots3, counts3)
