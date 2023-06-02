# -*- codeing = utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
path = "D:/数据分析/03.matplotlib课件和笔记/matplotlib课件和笔记/课件/09.折线与柱状组合图.xlsx"
plt.rcParams["font.sans-serif"] = ["SimHei"] #设置中文字体

read_data = pd.read_excel(path)
bu = plt.figure()
one = bu.add_subplot(111)
one.bar(read_data.班级,read_data.销售量,label = "销售量")
one.legend(loc = "upper left")
one.set_ylim([0,12500])

two = one.twinx()
two.plot(read_data.班级,read_data.毛利率,color = 'r',label = "毛利率")
my_per = ticker.PercentFormatter(1,2) #自行设定百分号
two.yaxis.set_major_formatter(my_per)
two.legend(loc="upper right")
two.set_ylim([0,1])
for x,y in zip(read_data.班级,read_data.毛利率):
    plt.text(x,y,str(round(y*100,2))+"%",c="r")
plt.show()