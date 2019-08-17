# 收入分析预测说明

1、程序：

+ Pre_income_ARIMR
+ Pre_income_ARMR
+ income_pre_main（运行函数）

2、数据库改动：

+ init：添加get_info_of_income(area, date)、insert_income_info(AREA,INCOME, BEGIN_TIME, END_TIME)、income_info(day, geohash, time_)函数，详细功能请看注释。

  另：init函数中已包含pagerank需求部分

+ base_table：新增New_Income_Table表格。存储各个区各个时段的收入信息，数据表内容请见附件SQL文件。

3、效果：

本次预测使用ARIMA、ARMR算法。

对于平稳、波动性小的数据，两个模型预测相近；对于波动性大的数据，两模型都表现一般。

对于不同的区，可分别对比两个算法的效果图。