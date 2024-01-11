import numpy as np
# np.random.normal(loc =0.0 , scale= 1.0,size = (5,4))    #生成随机正态分布数。
# loc：float类型，表示此正态分布的均值（对应整个分布中心）
# scale：float类型，表示此正态分布的标准差（对应于分布的密度，scale越大越矮胖，数据越分散；scale越小越瘦高，数据越集中）
# size：输出的shape，size=(k,m,n) 表示输出k维，m行，n列的数，默认为None，只输出一个值，size=100，表示输出100个值
print(np.random.normal(loc =100 , scale= 50.0,size = (50)))