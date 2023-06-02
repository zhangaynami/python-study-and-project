# -*- codeing = utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
pd.set_option("display.max_columns",None)

path = "D:/数据分析/python实战/tianchi_mobile_recommend_train_user/tianchi_mobile_recommend_train_user.csv"
save_path = "D:/数据分析/python实战/淘宝用户行为分析/"
r_d = pd.read_csv(path)

#数据清洗
r_d["time"] = pd.to_datetime(r_d["time"])
r_d["date"] = pd.to_datetime(r_d["time"].dt.date)
r_d["hour"] = r_d["time"].dt.hour

def user_pvuv_day(x = r_d):
    pv = x.groupby("date")["user_id"].count()
    uv =  x.groupby("date")["user_id"].nunique()
    bu = plt.figure()
    bu.add_subplot(211)
    pv.plot(x = "时间",y="PV")
    plt.xlabel("PV")
    bu.add_subplot(212)
    uv.plot(x = "时间",y = "UV")
    plt.xlabel("UV")
    plt.tight_layout()
    plt.savefig(save_path + "UV&PV_hour.png", dpi=300)
    plt.show()

def user_pvuv_hour(x = r_d):
    pv = x.groupby("hour")["user_id"].count()
    uv =  x.groupby("hour")["user_id"].nunique()
    bu = plt.figure()
    bu.add_subplot(211)
    pv.plot(x = "时间",y="PV")
    plt.xlabel("PV(百万)")
    bu.add_subplot(212)
    uv.plot(x = "时间",y = "UV")
    plt.xlabel("UV")
    plt.tight_layout()
    plt.savefig(save_path + "UV&PV_hour.png", dpi=300)
    plt.show()

def user_pvuv_hour_1212(x = r_d):
    pv = x[x["date"] == '2014-12-12'].groupby("hour")["user_id"].count()
    uv =  x[x["date"] == '2014-12-12'].groupby("hour")["user_id"].nunique()
    bu = plt.figure()
    bu.add_subplot(211)
    pv.plot(x = "时间",y="PV")
    plt.xlabel("12_PV")
    bu.add_subplot(212)
    uv.plot(x = "时间",y = "UV")
    plt.xlabel("12_UV")
    plt.tight_layout()
    plt.savefig(save_path + "UV&PV_hour_1212.png", dpi=300)
    plt.show()

#不同用户行为流量分析 统计在一天当中（按照每小时）用户发生的行为
def user_group(x=r_d):
    user_behave = x.groupby(["behavior_type","hour"])["user_id"].count()
    user_behave = user_behave.reset_index()

    plt.figure()
    sns.lineplot(x = 'hour',y="user_id",hue= "behavior_type",data = user_behave)
    plt.title("4种用户行为(万)")
    plt.savefig(save_path + "4种用户行为"
                            ".png", dpi=300)
    plt.show()
    # print( hour)
def user_group3(x=r_d):
    user_behave = x[x["date"] == '2014-12-12'].groupby(["behavior_type", "hour"])["user_id"].count()
    user_behave = user_behave.reset_index()

    plt.figure()
    sns.lineplot(x='hour', y="user_id", hue="behavior_type", data=user_behave[user_behave["behavior_type"] != 1])
    plt.title("用户行为")
    plt.savefig(save_path + "3种用户行为"
                            ".png", dpi=300)
    plt.show()
    # print( hour)

#转化
def change_rate(x = r_d):
    behavior_type = x.groupby(['behavior_type'])['user_id'].count()
    click_num, fav_num, add_num, pay_num = behavior_type[1],behavior_type[2],behavior_type[3],behavior_type[4]
    # rate_name = ["收藏转化率", "购物车转化率", "购买转化率"]
    # rate_num = [round(fav_num/click_num,4)*100,round(add_num/click_num,4)*100,round(pay_num/click_num,4)*100]
    fav_add_num = fav_num + add_num #购和收藏没有必然联系，因此我们把这两类合并在一起做分析
    rate_data = dict(rate_name = ["加购/收藏转化率", "点击 到 购买转化率", "加购/收藏 到 购买转化率"]
                     ,rate_num = [round(fav_add_num/click_num,4)*100,round(pay_num/click_num,4)*100,round(pay_num/fav_add_num,4)*100])
    i = px.funnel(rate_data,x="rate_num",y="rate_name")
    i.show()

def purchase_pc(x=r_d):
    data_user_buy = x[x["behavior_type"]==4].groupby("user_id")["behavior_type"].count()
    plt.figure()
    data_user_buy.plot(x="user_id")
    plt.savefig(save_path + "用户购买频次分析.png", dpi=300)
    plt.show()

#ARPU = 每日消费总次数 / 每日活跃用户数
def ARPU(x = r_d):
        # x["action"] = 1
        # data_user_arpu = x.groupby(['date','user_id','behavior_type'])['action'].count()
        # data_user_arpu = data_user_arpu.reset_index()
        # print(data_user_arpu.head())
    ap = x[x["behavior_type"]==4].groupby("date")["behavior_type"].count()/x.groupby("date")["user_id"].nunique()
    plt.figure()
    ap.plot(x = "date")
    plt.savefig(save_path + "ARPU.png", dpi=300)
    plt.show()

def ARPPU(x=r_d):

    ap = x[x["behavior_type"] == 4].groupby("date")["behavior_type"].count() / x[x["behavior_type"] == 4].groupby("date")["user_id"].nunique()
    plt.figure()
    ap.plot(x="date")
    plt.savefig(save_path + "ARPPU.png", dpi=300)
    plt.show()

#复购分析 复购率 = 复购用户数量 / 有购买行为的用户数量
def re_purchase(x=r_d):
    customers_re_purchase = x[x["behavior_type"] == 4].groupby("user_id")["date"].nunique()
    customers_purchase = customers_re_purchase[customers_re_purchase>1]
    re_purchase_rate = round(customers_purchase.count()/customers_re_purchase.count()*100,2)
    print(re_purchase_rate )

#复购周期分析
def re_purchase_zq(x=r_d):
    re_purchase_gr = x[x["behavior_type"] == 4].groupby(["user_id","date"])["behavior_type"].count().reset_index()

    # data_user_buy_date_diff = re_purchase_gr.groupby("user_id")["date"].apply(lambda i:i.sort_values().diff(1).dropna())
    # data_user_buy_date_diff = data_user_buy_date_diff.apply(lambda x: x.days)
    data_user_buy_date_diff = re_purchase_gr.groupby("user_id")["date"].apply(
        lambda i: i - i.shift())
    data_user_buy_date_diff = data_user_buy_date_diff.apply(lambda x: x.days)
    plt.xlabel('repeat_day_diff')
    plt.ylabel('count')

    # plt.figure()
    data_user_buy_date_diff.value_counts().plot(kind="line")
    plt.savefig(save_path + "复购周期.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    # user_pvuv_day(r_d)
    # user_pvuv_hour()
    # user_pvuv_hour_1212()
    # user_group(r_d)
    # user_group3(r_d)
    # change_rate(r_d)
    # purchase_pc(r_d)
    # ARPU(r_d)
    # ARPPU(r_d)
    # re_purchase(r_d)

    re_purchase_zq(r_d)
    pass






