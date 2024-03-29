import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
# Build a dataframe with 4 connections
df = pd.DataFrame({'from': ['A', 'B', 'C', 'A'], 'to': ['D', 'A', 'E', 'C']})
df

# Build your graph
# 绘制网络图，每次结果可能不一样
G = nx.from_pandas_edgelist(df, 'from', 'to')

# Plot it
nx.draw(G, with_labels=True)
plt.show()
