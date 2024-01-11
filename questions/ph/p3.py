import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.rcParams['font.family']='SimHei'
# matplotlib.rcParams['font.sans-serif']='SimHei'
dataset = pd.DataFrame(data=[[0.86 , 0.47, 0.88],
                [0.46,0.35,0.59],
                [0.62,0.44,0.75],
                [0.44,0.43,0.63],],
            index=[ 'Margale index','Simpson index ','Shannon-Wiener index','Pielou index'],
            columns=['tpyes1','types2','types3'])
radar_labels=dataset.index
nAttr=4
data=dataset.values #数据值
data_labels=dataset.columns
# 设置角度
angles=np.linspace(0,2*np.pi,nAttr,
                   endpoint= False)
data=np.concatenate((data, [data[0]]))
angles=np.concatenate((angles, [angles[0]]))
print(data)
print(angles)
# 设置画布
# 作图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig=plt.figure(facecolor="white",figsize=(10,6))
plt.subplot(111, polar=True)
# 绘图
plt.plot(angles,data,'o-',
         linewidth=1.5, alpha= 0.2)
# 填充颜色
plt.fill(angles,data, alpha=0.25)
plt.thetagrids(angles[:-1]*180/np.pi,
               radar_labels,1.2)
# plt.figtext(0.52, 0.95,'大学生通识能力分析',
#             ha='center', size=20)
# 设置图例
legend=plt.legend(data_labels,
                  loc=(1.1, 0.05),
                  labelspacing=0.5)
plt.setp(legend.get_texts(),
         fontsize='large')
plt.grid(True)
plt.savefig('tongshi.svg')
plt.show()