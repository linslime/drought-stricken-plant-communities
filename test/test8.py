import pandas as pd

df = pd.read_excel(r'D:\Desktop\one.xls')
data = df.values.tolist()
data = list(map(list, zip(*data)))
print(data)
for i in data:
    print(sum(i))
    print(len(i))