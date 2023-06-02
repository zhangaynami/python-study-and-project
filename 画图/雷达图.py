# -*- codeing = utf-8 -*-
import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np

path = "D:/数据分析/03.matplotlib课件和笔记/matplotlib课件和笔记/课件/22.雷达图.xlsx"
plt.rcParams["font.sans-serif"] = ["SimHei"] #设置中文字体
plt.rcParams['axes.unicode_minus'] = False#处理负数
read_data = pd.read_excel(path,index_col="姓名")
one = "姓名 == 'A01'"
two = "姓名 == 'A02'"

A01 = read_data.query(one)['分数']
A02 = read_data.query(two)['分数']
km = read_data.query(one)['科目']
jiaodu = np.linspace(0,2*np.pi,len(A01),endpoint=False)

A01 = np.concatenate((A01,[A01[0]]))
A02 = np.concatenate((A02,[A02[0]]))
km = np.concatenate((km,[km[0]]))
jiaodu = np.concatenate((jiaodu,[jiaodu[0]]))

# print(A02)
plt.style.use("ggplot")
bu = plt.figure()
tu =bu.add_subplot(111,polar=True)
tu.plot(jiaodu,A01,"bo-",linewidth =2,alpha = 0.25,label ="A01")
tu.fill(jiaodu,A01,"r",alpha = 0.25)
tu.plot(jiaodu,A02,"bo-",linewidth =2,alpha = 0.25,label ="A02")
tu.fill(jiaodu,A02,"g",alpha = 0.25)

plt.legend()

#设置标签
tu.set_thetagrids(jiaodu*180/np.pi,km)
tu.set_ylim(0,100)
plt.show()