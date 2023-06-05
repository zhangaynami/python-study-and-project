# -*- codeing = utf-8 -*-

"""倒入数据"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from math import pi
from sklearn.cluster import KMeans

#从sklearn导入聚类算法函数

"""
航空公司客户价值分析的LRFMC模型
在RFM模型中，消费金额表示在一段时间内客户购买该企业产品的金额的总和。
由于航空票价受到运输距离、舱位等级等多种因素的影响，同样消费金额的不同旅客对航空公司的价值是不同的，
例如，一位购买长航线、低等级舱位票的旅客与一位购买短航线、高等级舱位票的旅客相比，后者对于航空公司而言更有价值。
因此这个特征并不适用于航空公司的客户价值分析。
本案例选择客户在一定时间内累积的飞行里程M和客户在一定时间内乘坐舱位所对应的折扣系数的平均值C两个特征代替消费金额。
此外，航空公司会员入会时间的长短在一定程度上能够影响客户价值，所以在模型中增加客户关系长度L，作为区分客户的另一特征。
本案例将客户关系长度L、消费时间间隔R、消费频率F、飞行里程M和折扣系数的平均值C这5个特征作为航空公司识别客户价值的特征
记为LRFMC模型。其特征含义如下：
"""

# L：会员入会时间距观测窗口结束的月数
# R：客户最近一次乘坐公司飞机距观测窗口结束的月数
# F：客户在观测窗口内乘坐公司飞机的次数
# M：客户在观测窗口内累计的飞行里程
# C：客户在观测窗口内乘坐舱位所对于的折扣系数的平均值

plt.style.use('ggplot')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus']= False
pd.set_option("display.max_columns",None)

path1 = "D:/数据分析/航空公司/air_data.csv"
df = pd.read_csv(path1)

"""数据清洗"""

#剔除票价为0，平均折扣率不为0，总飞行公里大于0的记录
df = df[df['SUM_YR_1'].notnull() & df['SUM_YR_2'].notnull()] #票价非空值才保留

#只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
df1 = df["SUM_YR_1"] != 0
df2 = df["SUM_YR_2"] != 0
df3 = (df['SEG_KM_SUM'])== 0&(df['avg_discount']==0)
df = df[df1 | df2 | df3]

"""去除不必要的字段"""
df = df[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]

#3 数据变换
# L=LOAD_TIME-FFP_DATE(会员入会时间距观测窗口结束的月数=观测窗口的结束时间-入会时间（单位：月）)
# R=LAST_TO_END（客户最近一次乘坐公司距观测窗口结束的月数=最后一次。。。）
# F=FLIGHT_COUNT(观测窗口内的飞行次数)
# M=SEG_KM_SUM(观测窗口的总飞行里程)
# C=AVG_DISCOUNT(评价折扣率)

tmp = {
    "L" : (pd.to_datetime(df['LOAD_TIME']) - pd.to_datetime(df["FFP_DATE"])),
    "R": df["LAST_TO_END"],
    "F": df["FLIGHT_COUNT"],
    "M": df["SEG_KM_SUM"],
    "C": df["avg_discount"]
}
data = pd.DataFrame(data = tmp , columns = ["L","R","F","M","C"])
data['L'] = (data['L']/np.timedelta64(1,'D')).astype(int)
# 对数据进行归一化处理
normalized_df = (data - data.mean(axis = 0)) / data.std(axis=0)
normalized_df = pd.DataFrame(normalized_df)

# 计算每个会员的LRFMC得分
k = 5
#初始化Kmeans模型
kmodel = KMeans(n_clusters=k)
kmodel.fit(normalized_df)
kmeansCenters = pd.DataFrame(kmodel.cluster_centers_, columns = normalized_df.columns)
labelsCounts = pd.DataFrame(kmodel.labels_)[0].value_counts()

kmeansLabels = pd.DataFrame(labelsCounts, index = None)
kmeansLabels.columns = ['Num']
kmeansResult = pd.concat([kmeansCenters, kmeansLabels], axis=1)

kmeansResult['Group'] = ['群体一','群体二','群体三','群体四','群体五']
kmeansResult = kmeansResult[['Group','Num', 'L', 'R', 'F', 'M', 'C']].set_index("Group")
kmeansResult.columns = ['Num',"L：会员时长","R：最后乘机时间","F：飞行次数","M：飞行里层","C：评价折扣率"]

# 将会员分为5组
# group_labels = ['群体一', '群体二', '群体三', '群体四', '群体五']
group_labels = kmeansResult.index
sorted_df = kmeansResult.sort_values('Num', ascending=False)
sorted_df['Group'] = pd.qcut(kmeansResult['Num'], 5, labels=group_labels)
# 计算每组的平均得分
groupeds = sorted_df[["L：会员时长","R：最后乘机时间","F：飞行次数","M：飞行里层","C：评价折扣率"]]
# 绘制雷达图
categories = list(groupeds.columns)
num_vars = len(categories)

angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
for idx, group in enumerate(group_labels):
    values = groupeds.loc[group].values.tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, label=group)
    ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_yticklabels([])

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()