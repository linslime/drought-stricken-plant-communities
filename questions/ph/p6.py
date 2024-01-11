import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import numpy as np

def read():
    df = pd.read_excel(r'D:\Desktop\ww.xlsx')
    data = df.values.tolist()
    data = list(map(list, zip(*data)))
    return data

#主函数
if __name__ == "__main__":
    list = read()
    # print(list[0])
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = list[i][j] / 11

    # colors = ["#63b2ee", "#76da91" , "#f8cb7f" ,"#f89588", "#7cd6cf","#9192ab" ,"#7898e1","#efa666" ,"#eddd86","#9987ce","#63b2ee","#76da91"]
    colors = cm.coolwarm(np.arange(len(list[1:])) / len(list[1:]))
    # 作图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    labels = ["No contamination","Mild contamination","Moderate contamination","Heavy contamination","Extreme contamination"]
    for i in range(1,len(list)):
        plt.plot(list[0], list[i], color=colors[i - 1], linewidth=1.0, linestyle="-", label=labels[i - 1])  # 将散点连在一起
    # plt.plot(x, u2, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起

    # 添加图例
    font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
            'weight': 'normal',
            'size': 8,
            }
    plt.legend(loc=0, prop=font, labelspacing=1, frameon=True)
    plt.xlabel('time(y)')
    plt.ylabel('Average total biomass(g/m^2)')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()