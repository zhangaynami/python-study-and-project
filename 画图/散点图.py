# -*- codeing = utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
#显示全部数据
# pd.options.display.max_columns = None
path = "D:/数据分析/03.matplotlib课件和笔记/matplotlib课件和笔记/课件/16.散点图.xlsx"
plt.rcParams["font.sans-serif"] = ["SimHei"] #设置中文字体
read_data = pd.read_excel(path)
# print(read_data)
plt.scatter(read_data.身高,read_data.体重,s = read_data.身高,c= read_data.体重,marker="o")
plt.colorbar()
plt.show()