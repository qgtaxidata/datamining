import numpy as npimport pandas as pdimport Pre_income_ARIMRimport Pre_income_ARMRdef main_pre(date,area):    try:        pre_result = Pre_income_ARIMR.main_ARIMR(date,area)    except:        pre_result = Pre_income_ARMR.main_ARMR(date, area)if __name__ == '__main__':    main_pre('2017-02-15 08:32:48',11)          # 注：由于第四区：从化区收入量过少，预测结果都是0。