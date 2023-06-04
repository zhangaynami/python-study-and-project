# -*- codeing = utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus']= False
pd.set_option("display.max_columns",None)

path1 = "D:/数据分析/python实战/母婴/tianchi_mum_baby.csv"
path2 = "D:/数据分析/python实战/母婴/tianchi_mum_baby_trade_history.csv"
read_data1 = pd.read_csv(path1)
read_data2 = pd.read_csv(path2)

#数据预处理,设置正确的日期格式
read_data1["birthday"] =pd.to_datetime(read_data1.birthday.astype('str'))

#剔除性别未知
read_data1 = read_data1[read_data1.gender != 2]
# print(read_data1.birthday.describe()) #发现异常数据，存在1984年的数据
read_data1 = read_data1[read_data1["birthday"]> '2010-01-01']

#数据预处理，交易情况
# print(read_data2.head())
read_data2['day'] = pd.to_datetime(read_data2.day.astype("str"))
# 创建新列：月份、季度、年
read_data2['month'] = read_data2['day'].dt.month
read_data2['quarter'] = read_data2['day'].dt.quarter
read_data2['year'] = read_data2['day'].dt.year

#剔除购买量异常
read_data2 = read_data2[(read_data2.buy_mount >= 1) & (read_data2.buy_mount <= 189)]

# print(read_data2)
#
"""按照月份分组，计算每月的购买人数"""
# grouped = read_data2.groupby('month')['user_id'].nunique()
#
# # 绘制直方图
# plt.bar(grouped.index, grouped.values)
#
# # 设置图表标题和轴标签
# plt.title('month Purchase User Count')
# plt.xlabel('month')
# plt.ylabel('User Count')

# 展示图表
plt.show()
# 显示图形

"""查看11月内每天的销售情况"""
# read_data2 = read_data2[read_data2["month"]==11]
# read_data2["everyday"] = read_data2["day"].dt.day
# grouped = read_data2.groupby('everyday')['buy_mount'].sum()
#
# # 绘制直方图
# plt.bar(grouped.index, grouped.values)
#
# # 设置图表标题和轴标签
# plt.title('quarter Purchase User Count')
# plt.xlabel('quarter')
# plt.ylabel('User Count')
#
# # 展示图表
# plt.show()


"""统计购买次数"""
# grouped = read_data2.groupby('buy_mount')['user_id'].count()
# plt.bar(grouped.index, grouped.values)
# plt.show()

""" 查看各大类商品的销售情况"""
# category = read_data2.groupby("category_1")['buy_mount'].sum()
# plt.figure(figsize=(10, 6))
# plt.bar(category.index.astype(str),category.values)
# plt.title("Sales Volumn by Category")                                               #连接
#
# plt.xlabel("Category_1")
# plt.ylabel('Sales Volumn')                                                          # #统计用户年龄
# plt.show()

# """ 查看各大类商品下各子类商品的销售情况"""
# category = read_data2.groupby("category_1")['category_2'].nunique()
# plt.figure(figsize=(10, 6))
# plt.bar(category.index.astype(str),category.values)
# plt.title("Son Category")
#
# plt.xlabel("Category")
# plt.ylabel('Sales Volumn')                                                          # #统计用户年龄
# plt.show()

"""统计各类别下，子产品的平均销量"""
# category_buy_mount = read_data2.groupby("category_1")['buy_mount'].sum()
# son_category = read_data2.groupby("category_1")['category_2'].nunique()
# avg = category_buy_mount/son_category
# print(avg)
# plt.bar(avg.index.astype(str),avg.values)
# plt.show()

"""合并数据"""
# df = pd.merge(read_data2,read_data1)
#
"""统计用户性别 """
# gender_counts = df["gender"].value_counts()
# # 绘制饼图
# labels = ["Male", "Female"]
# sizes = [gender_counts[0], gender_counts[1]]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title("Gender Distribution")
# plt.axis('equal')
# plt.show()
"""男宝宝消费"""
# df = pd.merge(read_data2,read_data1)
# df = df[df["gender"] == 0]
#
# f_buy_amount = df.groupby("category_1")["buy_mount"].sum()
# # print(f_buy_amount)
# plt.pie(f_buy_amount.values,labels = f_buy_amount.index, autopct='%1.1f%%')
# plt.show()

"""女宝宝消费"""
# df = pd.merge(read_data2,read_data1)
# df = df[df["gender"] == 1]
#
# f_buy_amount = df.groupby("category_1")["buy_mount"].sum()
# # print(f_buy_amount)
# plt.pie(f_buy_amount.values,labels = f_buy_amount.index, autopct='%1.1f%%')
# plt.show()



