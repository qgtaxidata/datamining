from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import warnings
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import time
warnings.filterwarnings('ignore')

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
    result = model.predict(x_predict)
    return result
def GaussianNB_predict(X, y, x_predict):
    # 处理不平衡数据, 高斯分布预测
    gNB = GaussianNB()
    gNB.fit(X, y)
    result = gNB.predict(x_predict)
    return result
def MultinomialNB_pedict(X, y, x_predict):
    """多项式分布预测"""
    mNB = MultinomialNB()
    mNB.fit(X, y)
    result = mNB.predict(x_predict)
    return result
def BernoulliNB_pedict(X, y, x_predict):
    """多项式分布预测"""
    bNB = BernoulliNB()
    bNB.fit(X, y)
    result = bNB.predict(x_predict)
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
def hot_GaussianNB(all_lists):
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
        result = GaussianNB_predict(X, y, x_predict)
        predict_hot['lng'] = post_hot1[i]['lng']
        predict_hot['lat'] = post_hot1[i]['lat']
        predict_hot['count'] = int(result[0])
        predict_hots.append(predict_hot)
        counts += int(result[0])
    return predict_hots, counts
def hot_MultinomialNB(all_lists):
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
        result = MultinomialNB_pedict(X, y, x_predict)
        predict_hot['lng'] = post_hot1[i]['lng']
        predict_hot['lat'] = post_hot1[i]['lat']
        predict_hot['count'] = int(result[0])
        predict_hots.append(predict_hot)
        counts += int(result[0])
    return predict_hots, counts
def hot_BernoulliNB(all_lists):
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
        result = BernoulliNB_pedict(X, y, x_predict)
        predict_hot['lng'] = post_hot1[i]['lng']
        predict_hot['lat'] = post_hot1[i]['lat']
        predict_hot['count'] = int(result[0])
        predict_hots.append(predict_hot)
        counts += int(result[0])
    return predict_hots, counts


if __name__ == '__main__':
    json = [[{"lng":116.191031,"lat":39.988585,"count":12}, {"lng":116.191031,"lat":39.988585,"count":14}, {"lng":116.191031,"lat":39.988585,"count":12}],[{"lng":116.191031,"lat":39.988585,"count":10}, {"lng":116.191031,"lat":39.988585,"count":14}, {"lng":116.191031,"lat":39.988585,"count":8}],[{"lng":116.191031,"lat":39.988585,"count":16}, {"lng":116.191031,"lat":39.988585,"count":5}, {"lng":116.191031,"lat":39.988585,"count":6}]]
    predict_hots, counts = hot_line(json)
    predict_hots1, counts1 = hot_GaussianNB(json)
    predict_hots2, counts2 = hot_MultinomialNB(json)
    predict_hots3, counts3 = hot_BernoulliNB(json)
    print(predict_hots, counts)
    print(predict_hots1, counts1)
    print(predict_hots2, counts2)
    print(predict_hots3, counts3)

    # time1 = time.clock()
    # for i in range(2000):
    #     X = [[1], [2], [3]]
    #     y = [[2], [3], [4]]
    #     x_predict = [[4]]
    #     # a = line_predict(X, y, x_predict)
    #     a = BernoulliNB_pedict(X, y, x_predict)
    # time2 = time.clock()
    # print(time2 - time1)