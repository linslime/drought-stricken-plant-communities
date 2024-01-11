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
    print(x)
    print(y)

    # 作图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, y, color="#6456AA", linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.plot(x, u2, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起
    plt.xlabel('Population size')
    plt.ylabel('Average total biomass(g/m^2)')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()