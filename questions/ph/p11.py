import copy
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
        y[i] = y[i]*(1-x[i]/320)
    # data = list(map(list, zip(*data)))
    # print(data[1])
    # print(data)
    ll = []
    for i in range(len(data)):
        ll.append(data[i][1] *(1-i/320) * 1.2)
    print(ll)
    print(len(ll))
    x2 = [i + 1 for i in range(len(ll))]
    # 作图
    font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
            'weight': 'normal',
            'size': 10,
            }
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, y, color="red", linewidth=1.0, linestyle="-",label='the smaller environment')  # 将散点连在一起
    plt.plot(x2, ll, color="blue", linewidth=1.0, linestyle="-",label='the larger environment')  # 将散点连在一起
    plt.legend(loc=0, prop=font, labelspacing=2, frameon=True)
    plt.xlabel('Population size')
    plt.ylabel('Average total biomass(g/m^2)')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()