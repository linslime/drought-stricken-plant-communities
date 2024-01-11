import copy
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import numpy as np

df = pd.read_excel(r'D:\Desktop\four.xlsx')
data = df.values.tolist()
data = list(map(list, zip(*data)))

step = 0.01
start = 0
end = 1000

x = []
temp = start
while temp <= end:
    x.append(temp)
    temp += step

for i in range(len(data)):
    list = [7,12,5]
    for j in range(len(data[i])) :
        data[i][j] = data[i][j] / list[i]

colors = cm.coolwarm(np.arange(len(data)) / len(data))
# 作图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(x, data[0], color=colors[0], linewidth=1.0, linestyle="-", label='less frequent')  # 将散点连在一起
plt.plot(x, data[1], color=colors[1], linewidth=1.0, linestyle="-", label='more frequent')  # 将散点连在一起
plt.plot(x, data[2], color=colors[2], linewidth=1.0, linestyle="-", label='normal frequent')  # 将散点连在一起
# plt.plot(x, u2, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起

# 添加图例
font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
        'weight': 'normal',
        'size': 10,
        }
plt.legend(loc=0,prop=font,labelspacing=1,frameon=True)
plt.xlabel('time(y)')
plt.ylabel('biomass(g/m^2)')
plt.savefig("test.svg", dpi=300, format="svg")
plt.show()