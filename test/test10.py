import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

y = np.array([35, 25, 115, 15])
colors = cm.autumn(np.arange(4)/4)
plt.pie(y,
        labels=['A','B','C','D'], # 设置饼图标签
        # colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
        colors = colors,
        # explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%', # 格式化输出百分比
       )
plt.title("RUNOOB Pie Test")
# sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=result['avg'].min(), vmax=result['avg'].max()))
# plt.colorbar()
plt.show()

# import matplotlib.cm as cm  #导入库
#
# result = date.groupby(date.index.year).agg(sum=('成交笔数', 'sum'), avg=('换手率', 'mean'))  #计算每年成交笔数总计值，换手率均值
# plt.pie(result['sum'], colors=cm.ScalarMappable().to_rgba(result['avg']), labels=result.index, autopct='%3.1f%%') #根据换手率均值设置颜色绘制饼图
# plt.title('绘制每年股票成交笔数总计值为数值、标准化换手率为颜色的饼图')  #设置标题
# sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=result['avg'].min(), vmax=result['avg'].max()))
# plt.colorbar(sm)           #根据换手率均值的从小到大显示颜色
# plt.show()
