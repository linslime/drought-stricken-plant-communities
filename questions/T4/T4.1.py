import copy
import csv
import random

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import numpy as np

#步长，初始值，及终止值
step = 0.1
start = 0
end = 1000

# r = [0.15,0.09]
# p = [[1,0.5],[-0.3,1]]
# k = [100,80]
A0 = 50
s = 0.005
rain = []

r = [0.6668696767267881, 0.5706991627293867, 0.26942222618682365, 0.13643743205912318, 0.8782079861704143, 0.26392037495589027, 0.34989032459229863, 0.2033895313660936, 0.5717320955511114, 0.7831501420262225, 0.5217754633286357, 0.32034010586829487]
p = [[1, -0.011770541837162862, -0.46538918715689814, 0.23431488222354602, -0.022324107143222305, -0.33417644894038123, 0.14886709267442155, -0.47950273336353744, 0.37506339312205095, 0.41826206351027917, 0.4827435063309097, -0.15128812809301728], [-0.4682048078436508, 1, -0.21547611329250949, 0.33371927367650167, -0.01453921008635084, -0.36275422195068163, 0.3042249800082333, 0.13170363567840626, -0.18690813362627634, 0.016085380213701428, -0.2796537685075702, 0.3079113500517139], [0.3802034268992177, -0.09711020195816011, 1, 0.3629744976321174, 0.0711659019891745, 0.1899168215473389, -0.41078726425304335, -0.4043452267256752, -0.06970583125746788, -0.3459293836833194, 0.24739659770085431, 0.04567757560848151], [0.01519878892894877, 0.2781707134581509, 0.015557372861836116, 1, 0.2076005844123121, -0.2664903200183677, 0.34984258663113355, 0.4504588667489914, -0.18636145899074263, -0.32157629554434697, 0.13674178686611205, -0.1066017184528435], [0.4878020295097637, 0.0708802663579694, -0.015014337564556057, 0.26344925161297794, 1, -0.34256903978583686, 0.30987611691949746, -0.22436079367804318, 0.34792631675783137, 0.20690065822200698, 0.30462984866945597, 0.19268717230347798], [0.47537200271429214, 0.1343113003675468, 0.47624316094223695, -0.18261944968246246, 0.2184707558307839, 1, -0.4525199736363602, 0.1500390313585236, 0.10418830731809847, -0.25559220008875283, -0.2851289611719643, -0.11456445648009828], [0.37557032237360843, 0.3105027442282057, 0.08242916153655422, -0.1374866148016598, -0.21576668271920418, -0.400114018228515, 1, 0.09248273542900143, -0.16197237148108246, -0.02389795794186589, 0.008788706558699455, -0.36130051082268644], [0.3365355097333691, -0.06532278757396348, -0.009233269311941461, 0.0809826141111436, 0.05543186583577264, 0.20970978093713588, 0.40541191331969517, 1, 0.25627542698252426, 0.23883631242934023, -0.26422855273949475, -0.011798954297100983], [-0.4374258069575918, -0.26713330367526056, -0.23823326111804055, -0.39781434615696454, 0.2674544527751159, 0.28836042537452644, 0.40681763066062604, 0.4467362014170636, 1, -0.22021676122186085, -0.03222450621525197, 0.23349727107798945], [-0.2875850389800868, 0.24326190321022145, -0.3214187975011197, -0.32034031033419286, 0.03587258608131816, 0.1903154637746508, -0.33061348010065816, 0.026627752447007547, 0.0404360825603578, 1, 0.47563728967419927, -0.0893130834830762], [0.23038438703111652, -0.4779255842392691, 0.36790036541803595, 0.04118387970011672, -0.0082852945392079, 0.044587934413080066, 0.01804081520543921, -0.3603527227862894, 0.12223551892330575, 0.23144470877549939, 1, 0.04054885902243299], [0.1666753506492018, -0.11384855578256947, -0.2864927380815929, -0.34196498123904684, 0.29771050561826784, 0.4691265754546604, -0.027114541014387483, -0.4532753283977585, -0.437990145447977, 0.09710010296772842, 0.34677471607086263, 1]]
k = [132, 97, 114, 134, 126, 111, 77, 150, 92, 112, 64, 50]
# b = [0.000103781296377077, 0.000935081876176809, 0.0009494021700916436, 3.921770564269289e-05, 0.00025734336310932716, 0.00019540539018478176, 0.00038119576161350455, 0.0008595072419389677, 0.00018428993521074223, 0.0009145397963152647, 0.0006904623616030815, 0.0006929812964400821]
b = [0.004013048113139004, 0.002479837367329423, 0.004579224005203603, 0.0001942104501191183, 0.0015682466402680067, 0.002231073484490812, 0.003236671493893853, 0.0012510612966169022, 0.0011773282362232602, 0.0018944460622682313, 0.004502503816791083, 0.001207617191328818]
ppp = [0 for i in range(len(r))]
def read():
    global rain
    df = pd.read_excel(r'D:\Desktop\one.xls')
    data = df.values.tolist()
    data = list(map(list, zip(*data)))
    rain = data[0] + data[1] + data[2]
    # print(rain)

def change(n,m):
    global k
    global ppp
    if n != 1:
        k = [k[i] * random.uniform(n * 0.95,n * 1.05) for i in range(len(k))]
    if m != 0:
        ppp = [ppp[i] * random.uniform(m * 0.9,m + 1.1) for i in range(len(ppp))]

def K(list, i):
    return k[i] * list[-1] / 200

def f1(list, i):
    return r[i] * list[i + 1] * (1 - sum([p[i][j] * list[j + 1] / K(list,j) for j in range(len(list) - 2)])) -ppp[i] * list[i + 1]

def f2(list,i):
    return -1 * s * list[-1] - sum([list[j + 1] * b[j] for j in range(len(list) - 2)])

def RK4(t,variables,functions):
    n = len(variables)
    list = [[0 for i in range(n)] for j in range(4)]
    year = -1
    for i in range(len(t) - 1):
        parameter = [j[i] for j in variables]
        parameter.insert(0,t[i])

        for j in range(n):
            list[0][j] = functions[j](parameter,j)

        parameter = [variables[j][i] + step * list[0][j] / 2 for j in range(len(variables))]
        parameter.insert(0,t[i] + step / 2)
        for j in range(n):
            list[1][j] = functions[j](parameter,j)

        parameter = [variables[j][i] + step * list[1][j] / 2 for j in range(len(variables))]
        parameter.insert(0,t[i] + step / 2)
        for j in range(n):
            list[2][j] = functions[j](parameter,j)

        parameter = [variables[j][i] + step * list[2][j] for j in range(len(variables))]
        parameter.insert(0,t[i] + step)
        for j in range(n):
            list[3][j] = functions[j](parameter,j)

        parameter = [variables[j][i] + step / 6 * (list[0][j] + 2 * list[1][j] + 2 * list[2][j] + list[3][j]) for j in range(len(variables))]
        for j in range(n):
            variables[j][i + 1] = parameter[j]
        if int(t[i])//365 > year:
            copy_rain = copy.deepcopy(rain)
            year += 1
        variables[-1][i + 1] += copy_rain[int(t[i]) % len(rain)]
        copy_rain[int(t[i]) % len(rain)] = 0
    return variables

#主函数
if __name__ == "__main__":
    read()
    change(0.05,0.75)
    # print(k)
    x = []
    temp = start
    while temp <= end:
        x.append(temp)
        temp += step
    # u1 = [0 for i in range(len(x))]
    # u2 = [0 for i in range(len(x))]
    variables = [[0 for i in range(len(x))] for j in range(len(r) + 1)]
    # variables = [u1, u2]
    for i in range(len(r)):
        variables[i][0] = k[i] / 10
    variables[len(r)][0] = A0
        # print(variables[i][0])

    functions = [f1 for i in range(len(r))]
    functions.append(f2)
    # print(functions)
    variables = RK4(x,variables,functions)
    ww = [sum(variables[i][j] for i in range(len(variables))) for j in range(len(variables[0]))]
    # print(ww)
    haha = list(map(list, zip(*[ww])))
    with open("D:\Desktop\\ww.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(haha)
    # colors = ["#63b2ee", "#76da91" , "#f8cb7f" ,"#f89588", "#7cd6cf","#9192ab" ,"#7898e1","#efa666" ,"#eddd86","#9987ce","#63b2ee","#76da91"]
    colors = cm.gnuplot(np.arange(len(r))/len(r))
    #作图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.plot(x, ww, color=colors[0] ,linewidth=1.0, linestyle="-", label = '阅读人数')  # 将散点连在一起
    # plt.plot(x, u2, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起

    # 添加图例
    font = {'family': 'simhei',  # 这里必须要有第5行的操作前提
            'weight': 'normal',
            'size': 5,
            }
    plt.legend(loc=0,prop=font,labelspacing=1,frameon=True)
    plt.xlabel('time(y)')
    plt.ylabel('Average total biomass(g/m^2)')
    plt.savefig("test.svg", dpi=300, format="svg")
    plt.show()

    # 保存图为svg格式，即矢量图格式




