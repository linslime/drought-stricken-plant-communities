import math
import matplotlib.pyplot as plt

#步长，初始值，及终止值
step = 0.000001
start = 0
end = 1

G = 1
M = 1

def f1(list):
    print(list[0])
    return 2 * list[0]


def RK4(t,variables,functions):
        n = len(variables)
        print(n)
        list = [[0 for i in range(n)] for j in range(4)]
        for i in range(len(t) - 1):
            parameter = [j[i] for j in variables]
            parameter.insert(0,t[0])

            for j in range(n):
                list[0][j] = functions[j](parameter)

            parameter = [variables[j][i] + step * list[0][j] / 2 for j in range(len(variables))]
            parameter.insert(0,t[0] + step / 2)
            for j in range(n):
                list[1][j] = functions[j](parameter)

            parameter = [variables[j][i] + step * list[1][j] / 2 for j in range(len(variables))]
            parameter.insert(0,t[0] + step / 2)
            for j in range(n):
                list[2][j] = functions[j](parameter)

            parameter = [variables[j][i] + step * list[2][j] for j in range(len(variables))]
            parameter.insert(0,t[0] + step)
            for j in range(n):
                list[3][j] = functions[j](parameter)

            parameter = [variables[j][i] + step / 6 * (list[0][j] + 2 * list[1][j] + 2 * list[2][j] + list[3][j]) for j in range(len(variables))]
            for j in range(n):
                variables[j][i + 1] = parameter[j]
                # print(variables[j][i + 1])
            # print(variables)
        return variables

#主函数
if __name__ == "__main__":
    x = []
    temp = start
    while temp <= end:
        x.append(temp)
        temp += step

    u1 = [0 for i in range(len(x))]

    # u2[0] = math.pow(4 * g / R,0.5)
    u1[0] = 1

    variables = [u1]
    functions = [f1]

    variables = RK4(x,variables,functions)

    #作图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, u1, color="red" ,linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.plot(x, t, color="blue", linewidth=1.0, linestyle="-")  # 将散点连在一起
    plt.xlabel('时间/s')
    plt.ylabel('位移')
    plt.show()

    # #作图
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.plot(x, u2, color="red" ,linewidth=1.0, linestyle="-")  # 将散点连在一起
    # plt.xlabel('时间/s')
    # plt.ylabel('速度')
    # plt.show()
