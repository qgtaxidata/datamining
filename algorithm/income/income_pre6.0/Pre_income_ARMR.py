from db_tools import *from datetime import datetime, timedeltaimport matplotlib.pyplot as pltfrom statsmodels.tsa.arima_model import ARIMAimport numpy as npimport pandas as pdfrom statsmodels.tsa.arima_model import ARMAfrom statsmodels.tsa.seasonal import  seasonal_decomposeimport warningswarnings.filterwarnings('ignore')def loadData(rate_dict):    dataSet = get_traindata(rate_dict)  # 传入参数    paint_dataSet = []    i = 0    for data in dataSet:        time_ = data[1]        now_time = (get_date_time(time_[0]) + timedelta(hours=0.5))        paint_dataSet.append([i, data[0],str(now_time)])        i += 1    dataSet = pd.DataFrame(paint_dataSet, columns=['count','income', 'date'])   # print("经整理：", dataSet)    return dataSetdef get_date_time(strs):    return datetime.strptime(strs, '%Y-%m-%d %H:%M:%S')# 有修改def time_experate(date_time, hours, day):    """    区间选择器，这个hours表示将每天分成几个小时，day是表示一共前面历史天数    :param date_time:    :param hours:    :param day:    :return:返回所有遍历的时间区间    """    date_time = get_date_time(date_time) + timedelta(days=1)    pre_date_time = date_time - timedelta(days= day)    if pre_date_time < get_date_time('2017-02-01 00:00:00'):        pre_date_time = get_date_time('2017-02-01 00:00:00')        day = date_time - pre_date_time        day = int(str(day)[0])    num = int(24/hours)    time_stamp = []    for j in range(day):        for i in range(num):            date_time1 = pre_date_time + timedelta(hours= hours) * ( i + 1)            date_time2 = pre_date_time + timedelta(hours = hours) * i            # 时间区间            time_stamp.append([str(date_time2), str(date_time1)])        pre_date_time = pre_date_time + timedelta(days=1)    # print(time_stamp)    return time_stamp# 有修改def get_traindata(rate_dict, hours=1, day=7):    area = rate_dict['area']    date = rate_dict['date']    date = get_date_time(date) + timedelta(days=2)    # 代表某一天    date_time = str(date)[:11] + "00:00:00"    time_stamp = time_experate(date_time, hours, day)    #  print('时间区间：', time_stamp)    train_data = []    for time_ in time_stamp:        date = time_[0]        a = get_info_of_income(area, date)        if a == []:            train_data.append([0.0, time_])            print(train_data)        else:            train_data.append(get_info_of_income(area, date))    # print("数据库中取出的训练数据：", train_data)    return train_datadef get_MAPE(pre_result):    error_rate = 0.0    for one in pre_result:        if one[2] == 0:            pass        else:            error_rate += abs((one[2] - one[1]) / one[2])    # print(error_rate)    # print("误差为：" , (error_rate/len(pre_result)))class ModeDecomp(object):    def __init__(self, dataSet, test_size = 24):        data = dataSet.set_index('date')        data.index = pd.to_datetime(data.index)        self.dataSet = data        # input(dataSet)        self.test_size = test_size        self.train_size = len(self.dataSet) - self.test_size        self.income_train = self.dataSet['income'][:len(self.dataSet) - test_size]        # 差分        # print(self.income_train)        self.train = self._diff_smooth(self.income_train)        # 预测数据        self.test =  self.dataSet['income'][-test_size:]        print("测试集：",self.test)        print("训练集：",self.train)        #input()    def paint_draw(self):        smooth_income = np.array(self.income_train).tolist()        x = range(len(smooth_income))        plt.plot(x, smooth_income, 'r-')        plt.show()    # 对数据进行平滑处理    def _diff_smooth(self, dataSet):        dif = dataSet.diff(1)         # 差分序列        td = dif.describe()        high = td['75%'] + 1.5 * (td['75%'] - td['25%'])  # 定义高点阈值，1.5倍四分位距之外        low = td['25%'] - 1.5 * (td['75%'] - td['25%'])  # 定义低点阈值，同上        # 变化幅度超过阈值的点的索引        forbid_index = dif[(dif > high) | (dif < low)].index        i = 0        #print("异常点索引：",forbid_index)        while i < len(forbid_index) - 1:            n = 1  # 发现连续多少个点变化幅度过大，大部分只有单个点            start = forbid_index[i]  # 异常点的起始索引            # while ((i+n) <= len(forbid_index) - 1) & (forbid_index[i + n] == start + timedelta(minutes=60 * n)):            while forbid_index[i + n] == start + timedelta(minutes=60 * n):                n += 1                if (i + n) > len(forbid_index) - 1:                    break            i += n - 1            end = forbid_index[i]  # 异常点的结束索引            # print(i, n)            # print("关于异常点：", start, end)            # 用前后值的中间值均匀填充            value = np.linspace(dataSet[start - timedelta(minutes=60)], dataSet[end + timedelta(minutes=60)], n)            dataSet[start: end] = value            i += 1        return dataSet    # 分解(decomposing) 可以用来把时序数据中的趋势和周期性数据都分离出来:    def decomp(self, freq):        decomposition = seasonal_decompose(self.train, freq=freq, two_sided=False)        #  trend（趋势部分）        self.trend = decomposition.trend        # seasonal（季节性部分）        self.seasonal = decomposition.seasonal        #input(self.seasonal)        #  residual(残留部分)        self.residual = decomposition.resid        # print(self.trend,self.seasonal)        # decomposition.plot()        # plt.show()        # 生成描述性统计        d = self.residual.describe()        # print(d)        delta = d['75%'] - d['25%']        #input(d)        self.low_error, self.high_error = (d['25%'] - 1*delta, d['75%'] + 1*delta)    def trend_model(self):        self.trend.dropna(inplace=True)        self.trend_model = ARMA(np.log1p(self.trend),(1,0)).fit(disp = -1)        return self.trend_model    def predict_new(self):        """        预测新数据        :return:        """        n = self.test_size        self.pred_time_index = pd.date_range(start=self.train.index[-1], periods = n+1, freq='60min')[1:]        self.trend_pred = np.expm1(self.trend_model.forecast(n)[0])        pred_time_index = self.add_season()        return pred_time_index    def add_season(self):        '''        为预测出的趋势数据添加周期数据和残差数据        '''        self.train_season = self.seasonal[:self.train_size]        values = []        low_conf_values = []        high_conf_values = []        for i,t in enumerate(self.pred_time_index):            trend_part = self.trend_pred[i]            #相同时间的数据均值            season_part = self.train_season[self.train_season.index.time == t.time()].mean()            #趋势+周期+误差界限            predict = trend_part + season_part            low_bound = trend_part + season_part + self.low_error            high_bound = trend_part + season_part + self.high_error            values.append(predict)            low_conf_values.append(low_bound)            high_conf_values.append(high_bound)        self.final_pred = pd.Series(values, index=self.pred_time_index, name='predict')        self.low_conf = pd.Series(low_conf_values, index=self.pred_time_index, name='low_conf')        self.high_conf = pd.Series(high_conf_values, index=self.pred_time_index, name='high_conf')        return self.pred_time_index# 有修改def main_ARMR(date,area):    date = date + ' '+ '08:32:48'   # input(date)    rate_dict = {}    rate_dict['date'] = date    rate_dict['area'] = area    data = loadData(rate_dict)           #可调用getdata函数    print()    name = ['花都区', '南沙区', '增城区', '从化区', '番禺区', '白云区', '黄埔区', '荔湾区', '海珠区', '天河区', '越秀区']    mode = ModeDecomp(data, test_size=48)       #调节test_size可获取多天预测结果    mode.decomp(48)    mode.trend_model()    pred_time_index = mode.predict_new()    pred = mode.final_pred    test = mode.test    pred1 = np.array(pred).tolist()    test1 = np.array(test).tolist()    result = {}    result['title'] = name[area - 1] + '区域收入预测'    # input(name[area + 1]  + '区域收入预测')    result['income_forecast'] = {}    result['income_forecast']['x'] = []    result['income_forecast']['y'] = []    # 先存入前五天的真实数据    for i in range(len(mode.income_train)):        result['income_forecast']['x'].append(np.array(data.date).tolist()[i][0:10])        result['income_forecast']['y'].append(np.array(data.income).tolist()[i])    for i in range(len(pred)):        result['income_forecast']['x'].append(str(pred_time_index[i])[0:10])        result['income_forecast']['y'].append(pred[i])    print(result)    flag = 0    for i in test1:        if i ==0:            flag =1            break    if flag == 0:        # # print("最终测试结果：",pred)        plt.subplot(211)        # input(mode.dataSet)        plt.plot(mode.dataSet.index, mode.dataSet.income)        # plt.plot(mode.income_train)        plt.subplot(212)        test = pd.Series(test1, index=pred_time_index, name='test')        pred.plot(color='salmon', label='Predict')        test.plot(color='steelblue', label='Original')        mode.low_conf.plot(color='grey', label='low')        mode.high_conf.plot(color='grey', label='high')        plt.legend(loc='best')        plt.tight_layout()        plt.show()    else:        # # print("最终测试结果：",pred)        plt.subplot(211)        # input(mode.dataSet)        plt.plot(mode.dataSet[:-48].index, mode.dataSet[:-48].income)        # plt.plot(mode.income_train)        plt.subplot(212)        pred.plot(color='salmon', label='Predict')        mode.low_conf.plot(color='grey', label='low')        mode.high_conf.plot(color='grey', label='high')        plt.legend(loc='best')        plt.tight_layout()        plt.show()    return resultif __name__ == '__main__':    pre_result = main_ARMR('2017-02-15',8)    # get_MAPE(pre_result)