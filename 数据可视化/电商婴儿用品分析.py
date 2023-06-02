# -*- codeing = utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] =['Microsoft YaHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号


path1 = "D:/数据分析/python实战/电商数据分析/(sample)sam_tianchi_mum_baby.csv"
path2 = "D:/数据分析/python实战/电商数据分析/(sample)sam_tianchi_mum_baby_trade_history.csv"
read_data1 = pd.read_csv(path1)
read_data2 = pd.read_csv(path2)
df = read_data1.merge(read_data2,on = "user_id",how = "outer")

df["day"] = df["day"].astype("str")
df["day"] = pd.to_datetime(df["day"],errors="ignore")
df.drop(index = df[df["buy_mount"] > 30 ].index,inplace = True)
df.drop(index = df[df["buy_mount"] < 0 ].index,inplace = True)
df.dropna(subset = ["property"],inplace =True)
print(df.info())


def each_year_situation(df):
    '''
    观察各年度每月销售情况走势
    :param df:
    :return:
    '''
    df=df.groupby(pd.Grouper(key='day', freq='m')).sum()
    df['month']=df.index.month
    df['year']=df.index.year
    df=df[['year','month','buy_mount']]

    # 提取每月销量
    _x=df[df['year']==2014]['month']
    _x_2012=df[df['year']==2012]['month']
    _x_2015=df[df['year']==2015]['month']
    _y_2012=df[df['year']==2012]['buy_mount']
    _y_2013=df[df['year']==2013]['buy_mount']
    _y_2014=df[df['year']==2014]['buy_mount']
    _y_2015=df[df['year']==2015]['buy_mount']
    print(_y_2014.sum()/_y_2013.sum()-1)

    # 提取每月同比增速
    df_YOY=pd.DataFrame(
        {
            '2013':_y_2013.tolist(),
            '2014':_y_2014.tolist(),
        },
        index=_x
    )
    _y_2012.index=_x_2012
    _y_2015.index=_x_2015
    df_YOY=df_YOY.join(_y_2012)
    df_YOY=df_YOY.join(_y_2015,lsuffix='2012', rsuffix='2015')
    df_YOY.columns=['2013','2014','2012','2015']
    df_YOY=df_YOY.loc[:,['2012','2013','2014','2015']]
    df_YOY=df_YOY.pct_change(axis=1)*100

    plt.figure(figsize=(32,9),dpi=160)
    # 每月销量折线图
    ax1=plt.subplot(1,2,1)
    plt.plot(_x_2012, _y_2012, label='2012年')
    plt.plot(_x, _y_2013, label='2013年')
    plt.plot(_x, _y_2014, label='2014年')
    plt.plot(_x_2015, _y_2015, label='2015年')
    plt.title('月度销量情况')
    plt.grid(alpha=0.6)
    plt.xticks(_x,_x)
    plt.xlabel('月份')
    plt.ylabel('销量（件）')
    plt.legend(loc='upper left')

    # 同比增速折线图
    ax1=plt.subplot(1,2,2)
    _y_2015=df_YOY[df_YOY['2015']!=0]['2015']
    _x_2015=_x[:len(_y_2015.values)]
    plt.plot(_x,df_YOY['2013'],label='2013年')
    plt.plot(_x,df_YOY['2014'],label='2014年')
    plt.plot(_x_2015,_y_2015,label='2015年')
    plt.title('月度同比增速')
    plt.xticks(_x)
    plt.xlabel('月份')
    plt.ylabel('同比增速（百分比）')
    plt.legend()
    plt.grid(alpha=0.6)
    plt.show()

    def YOY_2014(df):
        '''
        计算2014年同比增速
        :param df:
        :return:
        '''
        df = df.groupby(pd.Grouper(key='day', freq='Y')).sum()
        df['年同比增速'] = df['buy_mount'].pct_change()
        print(df['buy_mount'])
        print(df['年同比增速'])

        def situation_2015_2(df):
            '''
            查看各年度春节前30日销售情况走势
            :param df:
            :return:
            '''
            df = df.groupby(by=pd.Grouper(key=('day'), freq='D')).sum()['buy_mount']
            _y_2013 = df['2013-1-10':'2013-2-15']
            _y_2014 = df['2014-1-1':'2014-2-6']
            _y_2015 = df['2015-1':'2015-2'][:-17:-1][::-1]
            _x = [i for i in range(len(_y_2013))]
            _x_label = ['闰月初一', '闰月初二', '闰月初三', '闰月初四', '闰月初五', '闰月初六', '闰月初七', '闰月初八', '闰月初九', '闰月初十', '闰月十一', '闰月十二',
                        '闰月十三', '闰月十四', '闰月十五', '闰月十六', '闰月十七', '闰月十八', '闰月十九', '闰月二十', '闰月廿一', '闰月廿二', '闰月廿三', '闰月廿四',
                        '闰月廿五', '闰月廿六', '闰月廿七', '闰月廿八', '闰月廿九', '闰月三十', '正月初一', '正月初二', '正月初三', '正月初四', '正月初五', '正月初六',
                        '正月初七', '正月初八']

            # 折线图-春节前30日每日销量情况比较
            plt.figure(figsize=(32, 9), dpi=160)
            ax1 = plt.subplot(1, 2, 2)
            plt.plot(_x, _y_2013, label='2013年')
            plt.plot(_x, _y_2014, label='2014年')
            plt.plot(_x[:len(_y_2015)], _y_2015, label='2015年')
            plt.xticks(_x, _x_label, rotation=45)
            plt.legend()
            plt.title('2013-2015年春节前30日每日销量情况比较')
            plt.grid(alpha=0.5)

            df_1 = pd.DataFrame(
                {
                    '2013': _y_2013[:16].sum(),
                    '2014': _y_2014[:16].sum(),
                    '2015': _y_2015.sum(),
                },
                index=[0]
            )
            df_1 = pd.concat([df_1, df_1.pct_change(axis=1)])
            df_1.index = ['销量', '同比增速']
            _x = df_1.columns

            # 春节前30日-前13日销量情况比较
            ax2 = plt.subplot(1, 2, 1)
            plt.bar(_x, df_1.loc['销量'], width=0.3, color='#ffaaa5', label='销量（左轴）')
            for x, y_2 in zip(_x, df_1.loc['销量']):
                plt.text(x, y_2 + 10, y_2, ha='center')
            ax2.set_ylabel('销量')
            ax2.set_xlabel('年份')
            plt.title('2013-2015年闰月初一到十五销量同比情况')
            plt.legend(loc='upper left')
            ax3 = ax2.twinx()
            _y_YOY = round((df_1.loc['同比增速'] * 100), 1)
            plt.plot(_x, _y_YOY, color='#a8e6cf', label='同比增速（右轴）')
            _y_YOY = _y_YOY.dropna()
            for x, y in zip(_y_YOY.index, _y_YOY):
                plt.text(x, y + 0.1, f'{y}%', ha='left')
            ax3.set_ylabel('同比增速')
            plt.legend(bbox_to_anchor=(0, 0.96), loc='upper left')
            plt.show()