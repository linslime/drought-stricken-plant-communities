import copy
import random

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import numpy as np

def read():
    df = pd.read_excel(r'D:\Desktop\two.xlsx')
    data = df.values.tolist()
    return data

#主函数
if __name__ == "__main__":
    data = read()
    list = [[] for i in range(1000)]

    x = []
    y = []
    for value in data:
        list[int(value[0])].append(value[1])
    for value in range(len(list)):
        if len(list[value]) != 0:
            x.append(value)
            y.append(sum(list[value])/len(list[value]))
    for i in range(len(y)):
        y[i] = y[i]*(1-x[i]/200)
    list = [[],[],[],[]]
    for i in range(len(y)):
        list[0].append((x[i] - 1)/200 /np.log(y[i]/200) *(1-x[i]/120)*4.2)
        aa = [random.randint(0,1000000) for i in range(x[i])]
        list[1].append((1 - sum([aa[i]/sum(aa) * aa[i]/sum(aa) for i in range(x[i])]))*(1-x[i]/400))

        list[2].append(-0.23*sum(aa[i]/sum(aa) * np.log(aa[i]/sum(aa)) for i in range(x[i]))*(1-x[i]/250))
        a = -0.23*sum(aa[i]/sum(aa) * np.log(aa[i]/sum(aa)) for i in range(x[i]))
        list[3].append(a/np.log(x[i]))
    print(x[0])
    # 作图
    # 添加图例
    font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
            'weight': 'normal',
            'size': 7,
            }

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    colors = cm.rainbow(np.arange(len(list)) / len(list))
    plt.plot(x, list[0], color="red", linewidth=1.0, linestyle="-",label='Margale index')  # 将散点连在一起
    plt.plot(x, list[1], color=colors[1], linewidth=1.0, linestyle="-", label='Simpson index')  # 将散点连在一起
    plt.plot(x, list[2], color=colors[2], linewidth=1.0, linestyle="-", label='Shannon-Wiener index')  # 将散点连在一起
    plt.plot(x, list[3], color=colors[3], linewidth=1.0, linestyle="-", label='Pielou index')  # 将散点连在一起
    # plt.plot(x, u2, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起
    plt.legend(loc=0, prop=font, labelspacing=2, frameon=True)

    plt.xlabel('Population size')
    plt.ylabel('Average total biomass(g/m^2)')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()