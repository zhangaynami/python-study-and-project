# -*- codeing = utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
path = "D:/数据分析/03.matplotlib课件和笔记/matplotlib课件和笔记/课件/12.日期.xlsx"
plt.rcParams["font.sans-serif"] = ["SimHei"] #设置中文字体
read_data = pd.read_excel(path)
plt.plot(read_data.日期,read_data.销售)
plt.grid(axis="x",color = "r",linestyle=":",linewidth=2)
plt.show()