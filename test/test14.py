import pandas as pd
df = pd.read_excel(r'D:\Desktop\p0.xlsx')
p0 = df.values.tolist()
print(p0[1][1])