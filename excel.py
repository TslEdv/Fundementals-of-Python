import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
data = pd.read_excel (r'python.xlsx')
print(data)
data['New_Col']=data['Number']*data['Price']
print(data)
group = data.groupby('Price')  
print(group.get_group(15))
x=data.Number
y=data.Price
stats = linregress(x, y)
m = stats.slope
b = stats.intercept
plt.figure(figsize=(10,10))
plt.scatter(x, y, marker='x')
plt.plot(x, m * x + b, color="blue", linewidth=3)
plt.xlabel("Number", fontsize=20)
plt.ylabel("Price", fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.savefig("linear-reg.png")

