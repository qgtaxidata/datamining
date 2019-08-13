from sklearn import linear_model
import warnings
warnings.filterwarnings('ignore')
from db_tools import *
from hot_Predict.line_return import *

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

def linear_models(line_paramter, time):
    return line_paramter[0]*time + line_paramter[1]

def linear_more_model(line_more_paramter, time):
    return line_more_paramter[0]*time + line_more_paramter[1]*time + line_more_paramter[2]*time + line_more_paramter[3]*time + line_more_paramter[4]*time + line_more_paramter[5]*time + line_more_paramter[6]*time + line_more_paramter[7]*time + line_more_paramter[8]*time + line_more_paramter[9]*time + line_more_paramter[10]

def Redge_model(redge_paramter, time):
    return redge_paramter[0]*time + redge_paramter[1]

def predict_hotmap(json):
    area = json['area']
    heat = json['heat']
    nowtime = json['nowTime']
    futureTime = json['futureTime']
    algorithm = json['algorithm']
    daytime = futureTime[-8:]
    time = float(daytime[:2]) * 60.0 + float(daytime[3:5]) + float(daytime[-2:]) / 60.0
    predict_map = {}
    if algorithm == 0:
        for i in range(len(heat)):
            try:
                geohash_point = heat[i]['geohash']
                paramter = get_operate_params(geohash_point[:5])[0]
                line_paramter  =  eval(paramter[0])
                result = int((linear_models(line_paramter, time)/32)*1/2 + heat[i]['count']*1/2)
                heat[i]['count'] = result
            except IndexError:
                heat[i]['count'] = heat[i]['count']
    elif algorithm == 1:
        for i in range(len(heat)):
            try:
                geohash_point = heat[i]['geohash']
                paramter = get_operate_params(geohash_point[:5])[0]
                line_paramter = eval(paramter[1])
                result = int((linear_more_model(line_paramter, time) / 32) * 1 / 2 + heat[i]['count'] * 1 / 2)
                heat[i]['count'] = result
            except IndexError:
                heat[i]['count'] = heat[i]['count']
    elif algorithm == 2:
        for i in range(len(heat)):
            try:
                geohash_point = heat[i]['geohash']
                paramter = get_operate_params(geohash_point[:5])[0]
                line_paramter = eval(paramter[1])
                result = int((Redge_model(line_paramter, time) / 32) * 1 / 2 + heat[i]['count'] * 1 / 2)
                heat[i]['count'] = result
            except IndexError:
                heat[i]['count'] = heat[i]['count']
    predict_map['area'] = area
    predict_map['heat'] = heat
    predict_map['futureTime'] = futureTime
    predict_map['nowtime'] = nowtime
    predict_map['algorithm'] = algorithm
    print(predict_map)
    return predict_map


if __name__ == '__main__':
    json = {'area': 1, 'heat': [{'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sc82', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s7qm', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s93n', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scxc', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2y0', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mpbm', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s37g', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s8bp', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0ssfx', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0whus', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t1e1', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s846', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s7rn', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s26w', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6pm', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t014', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2hb', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2gy', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sgr1', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4hz', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tkup', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mpcm', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s93z', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2gw', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sfpf', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4jr', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s738', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s733', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s71q', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4jp', 'count': 194}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sfpd', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6s6', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s71t', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3kk', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s730', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s732', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sc8b', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0semu', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s96x', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s96z', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t9ut', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sgd5', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0thc3', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4m2', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t037', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s96p', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s96r', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4m0', 'count': 16}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0skjq', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sunj', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s7tk', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9xm', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sf02', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4kb', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tj50', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t0sj', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t7py', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wmct', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t7rt', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mvsr', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t82u', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s97x', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6sp', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0skks', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6u0', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s97p', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6u1', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sbk4', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sckv', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6sk', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6d3', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ty', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mw4n', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6tv', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6v8', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wnh6', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s648', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6v4', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6dc', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9zv', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6dd', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t0ef', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t1wx', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s62g', 'count': 6}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t03r', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se08', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6e6', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sgde', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sf0q', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6tf', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4mb', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4mc', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6e4', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3my', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6e1', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9kp', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s63t', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s63p', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s63q', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ee', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6w7', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6w2', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t0fd', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sg3y', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mvdp', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s63k', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6du', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ug', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6dv', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tjxx', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ub', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0kyr2', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0ses0', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wm5j', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t4q5', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ez', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0krcp', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s76k', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0surg', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ey', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6vc', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se0n', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6en', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9kr', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wk0k', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6g2', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6ep', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6vb', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3qy', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9mr', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3qw', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t407', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s65r', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3qq', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0q47r', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6y8', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0susn', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s792', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s65p', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s77k', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se39', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se36', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6h9', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sf55', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0thfe', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t6cp', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s30z', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mtv4', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t415', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t63u', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3rw', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t417', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sspv', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se3b', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6z7', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tvu4', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sd1c', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t6w3', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3rq', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6z6', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se2x', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sspk', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se2u', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sbp6', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3c3', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9mx', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9mz', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3cm', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0krwy', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t40u', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s339', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mrqj', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0su54', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s31t', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s693', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0su51', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sdck', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0th89', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s31f', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t40e', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0th88', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s67j', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t40g', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6yf', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se3m', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6yc', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41y', 'count': 7}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0td0e', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41w', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scbx', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sfj8', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scbr', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41s', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scd6', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scbt', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41t', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41m', 'count': 10}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2rq', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scbp', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0kxck', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41e', 'count': 11}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0stcv', 'count': 4}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41g', 'count': 10}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6zm', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t41h', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se4x', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sd46', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tm1j', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3cv', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t3b0', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sdv1', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2cm', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sfjb', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9qp', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t3bc', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t445', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t66v', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t447', 'count': 12}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sccu', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0mu7e', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s21b', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sd54', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0suh9', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6jt', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sv7c', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3f5', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wjy0', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wk7m', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wjy1', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0wk7n', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scuj', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3fk', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sd5k', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3vv', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s366', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0stff', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0kxg6', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s34v', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s2v4', 'count': 3}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0suxu', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se6y', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scde', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s7mu', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9qx', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0kzyz', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0w02e', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0se6s', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s9qz', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tmh8', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t44y', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scvm', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scer', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t44q', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sceq', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tkbg', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scen', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t44n', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scuz', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scej', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0whsv', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t44k', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0te4y', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sd5t', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t44e', 'count': 5}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scuw', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t7kt', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0scuq', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3ft', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s92p', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s36w', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t1s7', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t45q', 'count': 2}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s36r', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s36t', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0sfn9', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s36n', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0tkce', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0t45n', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s6mz', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s3gy', 'count': 1}, {'longitude': None, 'latitude': None, 'time': None, 'geohash': 'ws0s91y', 'count': 2}], 'futureTime': '2017-02-01 15:00:00', 'nowTime': '2017-02-01 15:00:00', 'algorithm': 0}
    hot_map = predict_hotmap(json)
