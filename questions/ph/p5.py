import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

labels = np.array(['综合', '安全性', '体液免疫', '细胞免疫'])
# labels = np.array(['综合','KDA','发育','推进','生存','输出'])
labels = np.concatenate((labels, [labels[0]]))

nAttr = 4
# 特好 好 较好 差   100  85 70 55
# 3 3 1
# 2 3 4
# 4 3 1
# 2 2 3
# 75/3,
# 225/3
# 200/3
# 175/3
# 200/3

data1 = np.array([100 * (175 / 3) / (225 / 3), 85, 85, 25])
data2 = np.array([100 * (225 / 3) / (225 / 3), 50, 75, 100])
data3 = np.array([100 * (200 / 3) / (225 / 3), 100, 75, 25])
data4 = np.array([100 * (175 / 3) / (225 / 3), 50, 50, 75])
data5 = np.array([100 * (200 / 3) / (225 / 3), 75, 75, 50])

data2 = np.concatenate((data2, [data2[0]]))
data3 = np.concatenate((data3, [data3[0]]))
data4 = np.concatenate((data4, [data4[0]]))
data5 = np.concatenate((data5, [data5[0]]))

angles = np.linspace(0 + np.pi / 2, np.pi / 2 + 2 * np.pi, nAttr, endpoint=False)
data1 = np.concatenate((data1, [data1[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)

# for values in [values1, values2]:
# # 拼接数据首尾，使图形中线条封闭
#     values=np.concatenate((values,[values[0]]))
#     # 设置为极坐标格式
#     ax = fig.add_subplot(111, polar=True)
#     # 绘制折线图
#     ax.plot(angles, values, 'o-', linewidth=2)
#     # 填充颜色
#     ax.fill(angles, values, alpha=0.25)

#     # 设置图标上的角度划分刻度，为每个数据点处添加标签
#     ax.set_thetagrids(angles * 180/np.pi, feature)

#     # 设置雷达图的范围
#     ax.set_ylim(0,5)

plt.plot(angles, data1, '-', color='g', linewidth=1, alpha=0.45, label='灭活疫苗')
plt.fill(angles, data1, facecolor='g', alpha=0.25)
plt.thetagrids(angles * 180 / np.pi, labels)

plt.plot(angles, data2, '-', color='y', linewidth=1, alpha=0.45, label='减毒活疫苗')
plt.fill(angles, data2, facecolor='y', alpha=0.25)
# plt.thetagrids(angles*180/np.pi,labels)

plt.plot(angles, data3, '-', color='r', linewidth=1, alpha=0.45, label='亚单位疫苗')
plt.fill(angles, data3, facecolor='r', alpha=0.25)
# plt.thetagrids(angles*180/np.pi,labels)

plt.plot(angles, data4, '-', color='grey', linewidth=1, alpha=0.45, label='活载体疫苗')
plt.fill(angles, data4, facecolor='grey', alpha=0.25)
# plt.thetagrids(angles*180/np.pi,labels)

plt.plot(angles, data5, '-', color='blue', linewidth=1, alpha=0.45, label='核酸疫苗')
plt.fill(angles, data5, facecolor='blue', alpha=0.25)
# plt.thetagrids(angles*180/np.pi,labels)


plt.figtext(0.515, 0.95, '各种疫苗特性2', ha='center')

plt.legend(loc='best')
plt.grid(True)
# plt.savefig("各种疫苗特性.png",dpi=600)
plt.show()