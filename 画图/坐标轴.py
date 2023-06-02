# -*- codeing = utf-8 -*-
# import matplotlib.pyplot as plt
# bu,tu = plt.subplots(1,1)
# #设置轴的颜色
# tu.spines["top"].set_color("none")
# tu.spines["right"].set_color("none")
# tu.spines["left"].set_color("g")
# tu.spines["bottom"].set_color("r")
#轴反转
# zhou = plt.gca()
# zhou.invert_yaxis()
# zhou.invert_xaxis()
#取消坐标
# tu.set_xticks([])
# tu.set_yticks([])
# plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
path = "D:/数据分析/03.matplotlib课件和笔记/matplotlib课件和笔记/课件/17.直方图.xlsx"
plt.rcParams["font.sans-serif"] = ["SimHei"] #设置中文字体
plt.rcParams['axes.unicode_minus'] = False#处理负数
read_data = pd.read_excel(path)
bu, tu =plt.subplots(1,1)
tu.plot(read_data.序号,read_data.身高)
# plt.locator_params("x",nbins=5) #对轴进行划分
# plt.gca().locator_parmas("x",nbins=5)
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(7))
plt.show()