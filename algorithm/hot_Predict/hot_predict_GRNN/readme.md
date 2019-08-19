# 神经网络之热力图说明

+ 算法实现程序为：hot_predict_GRNN.py。

+ 实现该算法时在数据库的init程序及base_table程序中均有增添函数。其中，init中添加了get_hot_info_1(get_)、get_hot_info_2(get，date__)函数，base_table中添加了class new_table_for_hot(Base)。

+ 本算法实现需要在数据库中建表，用于存储、提取模型的训练集。详细SQL文件可见文件夹内。
+ 运行效果图可见文件夹内。由于本算法先通过预测五级geohash块的订单量，再按比例划分七级块的订单量，故效果图中前面部分可适当忽略。（其为五级块预测结果）。