# -*- codeing = utf-8 -*-
import  matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")
jaodu = np.array([0.25,0.75,1,1.5,0.25])
zhou = [20,60,40,80,20]
plt.polar(jaodu*np.pi,zhou,"ro-")
plt.fill(jaodu*np.pi,zhou,"ro",alpha = 0.25)
plt.ylim(0,100)
plt.show()