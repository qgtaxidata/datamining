"""
the pysql file
"""
import pymysql
import requests
import warnings
warnings.filterwarnings('ignore')

db1 = pymysql.connect('10.21.48.11', 'qgtaxi', 'qgtaxi_2018', 'operate_his')
db2 = pymysql.connect('localhost', 'fkylin', 'rosehip@10', 'qgtaxi')
cursor1 = db1.cursor()
cursor2 = db2.cursor()

sql1 = 'insert into operate_his'
sql2 = '(ID, EQUIPMENT_ID, PLATENO, COMPANY_ID, TEAM_CODE, EMPTY_MILE, EMPTY_BEGIN_TIME, ' \
      'WORK_BEGIN_TIME, WORK_END_TIME, UNIT_PRICE, LOAD_MILE, SLOW_COUNT_TIME, OPERATE_MONEY, EVALUATE, ' \
      'TRADE_CODE, GET_ON_LONGITUDE, GET_ON_LATITUDE, GET_OFF_LONGITUDE, GET_OFF_LATITUDE, TIME_REPRE, ' \
      'GEOHASH5, MIN_REPRE, GEOHASH7, GEOEND7, CHAUFFEUR_NO, ROW_KEY) value (%s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
      '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

sql_create_table = "CREATE TABLE `operate_his%d`  ( \
  `ID` bigint(20) NOT NULL AUTO_INCREMENT, \
  `EQUIPMENT_ID` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL, \
  `PLATENO` varchar(24) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL, \
  `COMPANY_ID` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `TEAM_CODE` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `EMPTY_MILE` varchar(24) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `EMPTY_BEGIN_TIME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `WORK_BEGIN_TIME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `WORK_END_TIME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `UNIT_PRICE` varchar(7) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `LOAD_MILE` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `SLOW_COUNT_TIME` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `OPERATE_MONEY` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `EVALUATE` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `TRADE_CODE` varchar(96) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GET_ON_LONGITUDE` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GET_ON_LATITUDE` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GET_OFF_LONGITUDE` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GET_OFF_LATITUDE` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `TIME_REPRE` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GEOHASH5` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `MIN_REPRE` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GEOHASH7` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `GEOEND7` varchar(765) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,\
  `CHAUFFEUR_NO` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, \
  `ROW_KEY` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL, \
  PRIMARY KEY (`ID`) USING BTREE, \
  INDEX `PLATENO`(`PLATENO`) USING BTREE, \
  INDEX `WORK_BEGIN_TIME`(`WORK_BEGIN_TIME`) USING BTREE, \
  INDEX `GEOHASH5`(`GEOHASH5`) USING BTREE, \
  INDEX `ROW_KEY`(`ROW_KEY`) USING BTREE \
) ENGINE = MyISAM CHARACTER SET = sjis COLLATE = sjis_japanese_ci ROW_FORMAT = Dynamic;"

for db_number in range(22, 60):
    num = 500
    print('-' * 25)
    print('--- selecting the %dth data ---' % db_number)
    data = cursor1.execute('select * from operate_his%d' % db_number)
    print('--- selection completed ---')
    print('-' * 25)
    cursor2.execute(sql_create_table % db_number)
    print('--- storing %dth data ---' % db_number)
    for i in range(int(data / num)):
        print('database: \t%d\tprocess: \t%d / %d' % (db_number, i, int(data / num)))
        data_part = cursor1.fetchmany(num)
        cursor2.executemany(sql1 + str(db_number) + sql2, data_part)

    data_remain = cursor1.fetchall()
    cursor2.executemany(sql1 + str(db_number) + sql2, data_remain)
    print('--- storing completed ---')
    print('-' * 25)

print('--- bunch storing completed ---')
print('-' * 25)
db2.commit()

db1.close()
db2.close()
