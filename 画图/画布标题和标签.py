# -*- codeing = utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams["font.sans-serif"] = ["SimHei"] #设置中文字体
plt.subplot(221)
plt.plot(["A","B","C"],[1,2,3],"o")
a = dict(facecolor='yellow',pad =5,alpha=0.2)
plt.xlabel("Lpp",bbox=a)
plt.subplot(222)
plt.subplot(223)
plt.subplot(224)
plt.suptitle("Xsh",fontsize = 20,fontweight="bold",color = "r")
plt.subplots_adjust(left=0.2,top=0.8,wspace=0.8,hspace=0.8,bottom=0.1)
plt.show()