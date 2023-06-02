# -*- codeing = utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus']= False

path = "D:/数据分析/python实战/order2021.xlsx"
read_data = pd.read_excel(path)
pd.set_option("display.max_columns",None)

#数据清洗
# print(read_data.info())
# print(read_data.describe())
read_data.columns = read_data.columns.str.strip() #去空字符
read_data.dropna(inplace = True)
abnormal = read_data[np.where(read_data["付款金额"]<0,True,False)].index
read_data.drop(abnormal ,inplace = True)
# print(read_data)

#新增日期列
read_data["订单日期"] = pd.to_datetime(read_data["付款时间"],format = "%Y-%m-%d").dt.date
read_data['月份'] = read_data["订单日期"].astype('datetime64[M]') #只看月份
# print(read_data.head())

# 筛选未退订单
df1 = read_data[np.where(read_data["是否退款"] == "否",True,False)]
df1["订单日期"].astype('datetime64[M]')
# print(df1)
# #用户整体消费趋势分析
# #月产品购买数量
# bu = plt.figure(figsize = (30,20),dpi=150)
# bu.tight_layout()
# plt.subplot(221)
# one = plt.plot(df1.groupby("月份")['商品编号'].count())
# plt.title("月产品购买数量")
#
# #每月产品消费金额
# plt.subplot(222)
# two = plt.plot(df1.groupby("月份")['付款金额'].sum())
# plt.title("每月产品消费金额")
#
# #每月产品消费次数
# plt.subplot(223)
# three = plt.plot(df1.groupby("月份")['用户名'].count())
# plt.title("每月产品消费次数")
#
# #每月产品消费人数
# plt.subplot(224)
# four = plt.plot(df1.groupby("月份")['用户名'].nunique())
# plt.title("每月产品消费人数")
# plt.show()
#————————————————————————————————————————————————————————————#
# 用户个体的消费分析
# 订单金额
# bu2 = plt.figure(figsize=(12,6),dpi=120)
# #hist 分组并绘制直方图
# plt.hist(df1["订单金额"],label ="订单金额",bins=40,color = "b",edgecolor = "w",alpha = 0.3,density=True,range=(1,6000))
# plt.title("订单金额分布")
#————————————————————————————————————————————————————————————#
# 付款金额
# bu3 = plt.figure(figsize=(12,6),dpi=120)
# #hist 分组并绘制直方图
# plt.hist(df1["付款金额"],label ="付款金额",bins=40,color = "b",edgecolor = "w",alpha = 0.3,density=True,range=(1,6000))
# plt.title("付款金额分布")
# plt.show()
#————————————————————————————————————————————————————————————#

# #用户累计消费金额占比分析（用户的贡献度）
# # 进行用户分组，取出消费金额，进行求和，排序，重置索引
# user_consum = df1.groupby('用户名')["付款金额"].sum().sort_values().reset_index()
# # 每个用户消费金额累加 cumsum函数
# user_consum['付款金额累加'] = user_consum["付款金额"].cumsum()
# amount_total = user_consum['付款金额累加'].max() # 消费金额总值
# user_consum["prop"] = user_consum.apply(lambda x:x['付款金额累加']/amount_total,axis=1)
# # print(user_consum)
# bu4 =plt.figure(figsize=(8,8),dpi=150)
# plt.title("用户贡献度")
# plt.plot(user_consum["prop"])
#————————————————————————————————————————————————————————————#
#首次购买时间
# bu5 =plt.figure(figsize=(8,4),dpi=150)
# df1.groupby(by='用户名')["订单日期"].min().value_counts().plot()
# plt.title("首次购买时间")
# plt.show()
#————————————————————————————————————————————————————————————#
# bu6 =plt.figure(figsize=(8,4),dpi=150)
# df1.groupby(by='用户名')["订单日期"].max().value_counts().plot()
# plt.title("最后购买时间")
# plt.show()
#————————————————————————————————————————————————————————————#
# # 构建RFM模型,RFM模型是利用的R消费间隔（Recency）、F消费频率（Frequency）、M消费金额（Monetary）三项指标来衡量客户价值的手段。
# # 数据透视表：统计最近交易时间、交易次数、交易金额
# rfm = df1.pivot_table(index="用户名",values=["订单日期","订单号","付款金额"],aggfunc={"订单日期":"max","订单号":"count","付款金额":"sum"})
# rfm["R"] = (rfm["订单日期"].max() - rfm["订单日期"])/np.timedelta64(1,"D")
# rfm.rename(columns = {"订单号":"F",'付款金额':'M'},inplace=True)
#
# # RFM计算方式 ：每一列数据减去数据所在列的平均值（有正有负），根据结果值与1作比较，如果>=1，设置为1，否则为0
# def rfm_func(x):   #x代表每一列数据
#     level = x.apply(lambda x:"1" if x >= 1 else "0")
#     label = level["R"] + level["F"] + level["M"]
#     d = {
#         '111':'重要价值客户',
#         '011':'重要保持客户',
#         '101':'重要发展客户',
#         '001':'重要挽留客户',
#         '110':'一般价值客户',
#         '010':'一般保持客户',
#         '100':'一般发展客户',
#         '000':'一般挽留客户'
#     }
#     result = d[label]
#     return result
# #每一列数据减去数据所在列的平均值（有正有负）
# rfm["label"] = rfm[["R","F","M"]].apply(lambda x:x-x.mean()).apply(rfm_func,axis = 1)
# # print(rfm.head())
#
# plt.figure(figsize=(8,4),dpi= 120)
# for label,group in rfm.groupby("label"):
#     x = group["F"]
#     y = group["M"]
#     plt.scatter(x,y,label = label)
#
# plt.legend()
# plt.xlabel("消费频率")
# plt.ylabel("消费金额")
# plt.show()
#————————————————————————————————————————————————————————————#
#新老，活跃，回流用户分析

#统计每月都消费量
# pivoted_counts = df1.pivot_table(index="用户名",columns= "月份",values="订单日期",aggfunc="count").fillna(0)
# # print(pivoted_counts.head())
# df_punchase = pivoted_counts.applymap(lambda x:1 if x>0 else 0)
# print(df_punchase)

# # 判断是否为 新、活跃、不活跃、回流用户
# def active_status(data):  # data整行数据 共12列 即一个用户的12个月的消费记录
#     status = []  # 负责存储用户 12 个月的状态：unreg|new|active|unactive|return
#     for i in range(12):
#         # 本月没有消费
#         if data[i] == 0:
#             if len(status) == 0:  # 前面没有任何记录（21年1月份）
#                 status.append('unreg')
#             else:  # 开始判断上一个月状态
#                 if status[i - 1] == 'unreg':  # 一直未消费过
#                     status.append('unreg')
#                 else:  # 只要本月没有消费当前的为0且不是unreg 只能为unactive
#                     status.append('unactive')
#         # 本月有消费==1
#         else:
#             if len(status) == 0:  # 前面没有任何记录（21年1月份）
#                 status.append('new')
#             else:  # 之前有过记录  开始判断上一个月状态
#                 if status[i - 1] == 'unactive':  # 上个月没有消费
#                     status.append('return')
#                 elif status[i - 1] == 'unreg':  # 以前没有消费过
#                     status.append('new')
#                 else:
#                     status.append('active')
#     return pd.Series(status, df_punchase.columns)  # 值为status 列名为df_purchase中的列名
#
#
# purchase_states = df_punchase.apply(active_status, axis=1)  # axis=1 朝列的方向读取
# # print(purchase_states.head())
# purchase_states_ct = purchase_states.replace("unrge",np.NaN).apply(lambda x:pd.value_counts(x))
# print(purchase_states_ct)

# plt.figure(figsize=(10,10),dpi=100)
# purchase_states_ct.T.fillna(0).plot.area()
# plt.show()

#回流用户占比
# plt.figure(figsize=(10,10),dpi=100)
# rate = purchase_states_ct.T.fillna(0).apply(lambda x:x/x.sum(),axis = 1 )
# plt.plot(rate["return"],label = "return")
# plt.plot(rate["active"],label = "active")
# plt.legend()
# plt.show()
#————————————————————————————————————————————————————————————#

#用户购买周期

# # 计算购买周期
a = df1.groupby('用户名')

print(df1)
order_diff = df1.groupby(by='用户名').apply(lambda x:x['订单日期']-x['订单日期'].shift()) #当前订单日期 — 上一次订单日期
print(order_diff.head())
# plt.figure(figsize=(10, 10), dpi=100)
# (order_diff/np.timedelta64(1,'D')).hist(bins=20)
# plt.show()

#复购率分析
# # 计算方式： 用户最后一次购买 — 第一次购买的日期  如果差值=0 说明用户只够买了一次
# user_life = df1.groupby(by='用户名')['订单日期'].agg(['min','max'])
# plt.figure(figsize=(10, 10), dpi=100)
# (user_life['max'] == user_life['min']).value_counts().plot.pie(autopct='%1.1f%%') # 判断只够买一次的用户占比  格式化一位小数
# plt.legend(['仅消费一次','多次消费'])
# plt.show()
#————————————————————————————————————————————————————————————#
# # 绘制所有用户生命周期直方图+多次消费
# user_life = df1.groupby("用户名")["订单日期"].agg(["min","max"])
# plt.figure(figsize=(8,4),dpi=120)
# one = plt.subplot(121)
# ((user_life["max"] - user_life["min"])/np.timedelta64(1,"D")).hist(bins = 30) #计算一个用户最大的消费间隔
# plt.title("用户生命周期直方图")
# plt.xlabel("生命周期")
# plt.ylabel("用户数")
#
# two = plt.subplot(122)
# # print(user_life.head())
# u_1 = (user_life["max"] - user_life["min"]).reset_index()[0]/np.timedelta64(1,"D")
# u_1[u_1>0].hist(bins=25)
# # print(u_1)
# plt.title("多次消费的用户生命周期")
# plt.show()

#————————————————————————————————————————————————————————————#
#复购率分析
# plt.figure()
# purchase_r = pivoted_counts.applymap(lambda x:1 if x>1 else np.NaN if x == 0 else 0)
# (purchase_r.sum()/purchase_r.count()).plot(figsize=(12,6))
# plt.title("复购率分析")
# plt.show()
#————————————————————————————————————————————————————————————#
#回购率分析
# 计算方式：在一个时间窗口内进行了消费，在下一个窗口又进行了消费
# 1：回购用户：当前月消费了，下个月又消费了  0：当前月消费 下个月未消费   nan：当前月未消费
# def purchase_back(data):
#     status = [] #存储用户回购率状态
#     for i in range(11):
#         # 当前月消费了
#         if data[i] == 1:
#             if data[i+1] ==1:
#                 status.append(1) # 回购用户
#             elif data[i+1] == 0:
#                 status.append(0) # 下个月未消费
#         # 当当前月未消费
#         else:
#             status.append(np.NaN)
#     status.append(np.NaN)  # 填充最后一列数据
#     return pd.Series(status,df_punchase.columns)
# purchase_b = df_punchase.apply(purchase_back,axis=1)
# # print(purchase_b.head())
#
# plt.figure(figsize=(20,15),dpi= 200)
# plt.subplot(211)
# (purchase_b.sum()/purchase_b.count()).plot(label = "回购率")
# (purchase_r.sum()/purchase_r.count()).plot(label = "复购率")
# plt.title("用户复购率和回购率对比图")
# plt.ylabel("百分比")
# plt.legend()
#
# plt.subplot(212)
# plt.plot(purchase_b.sum(),label="回购人数")
# plt.plot(purchase_b.count(),label="复购人数")
# plt.xlabel("月份")
# plt.ylabel("人数")
# plt.legend()
# plt.show()
#
