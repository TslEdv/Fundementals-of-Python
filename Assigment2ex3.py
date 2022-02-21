import pandas as pd 

data1 = pd.read_excel (r'conc1.xlsx')
data2 = pd.read_excel (r'conc2.xlsx')
frames=[data1, data2]
result = pd.concat(frames)
print(result)