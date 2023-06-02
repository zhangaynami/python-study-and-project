# -*- codeing = utf-8 -*-
# -*- codeing = utf-8 -*-
# import pandas as pd
# path = "D:/数据分析/02.Pandas课件/Pandas课件/课件/pandas教程/课件030-031/环比.xlsx"
# read_data = pd.read_excel(path,"Sheet1")
# last_month = read_data.销售金额.shift() #shift向下移动
# hb = read_data.销售金额 - last_month
# read_data["环比增长金额"] = hb
# print(read_data)

# import pandas as pd
# path = "D:/数据分析/02.Pandas课件/Pandas课件/课件/pandas教程/课件030-031/环比.xlsx"
# read_data = pd.read_excel(path,"Sheet2")
# def gs(new_data):
#     new_data["环比"] = new_data.金额 - new_data.金额.shift()
#     return new_data
# read_data2 = read_data.sort_values(["城市","月份"]).groupby(["城市"]).apply(gs)
# print(read_data2)

import pandas as pd
path = "D:/数据分析/02.Pandas课件/Pandas课件/课件/pandas教程/课件030-031/同比.xlsx"
read_data = pd.read_excel(path,"Sheet1")
year = read_data["日期"].dt.year
data2 = pd.pivot_table(read_data,index="店号",values="金额",columns=year,aggfunc="sum")
date2 = data2[2018]/data2[2019]-1
print(date2)
