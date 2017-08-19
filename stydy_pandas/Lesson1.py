# -*- coding：utf-8 -*-

#导入库
from pandas import DataFrame,read_csv
import  numpy as np
import  matplotlib.pyplot as plt
import  pandas as pd
import  matplotlib
import  sys

#打印版本号
print('Python version'+sys.version)
print('Pandas version'+pd.__version__)
print('Matplotlib version'+matplotlib.__version__)
print('Numpy version'+np.__version__)

#创建数据
names=['Bob','Jery','heck','tery']
birth_nums=[178,560,124,977,325]
BabyDataSet=list(zip(names,birth_nums))
df=pd.DataFrame(BabyDataSet,columns=['names','bbirth_nums'])
#print(df)
df.to_csv('Birth_num.csv',index=False,header=False)

#获取数据

Location=r'E:\data_Vis\code\stydy_pandas\Birth_num.csv'
df=pd.read_csv(Location,names=['names','Birth_nums'])
#print(df)

#查看数据类型
print('全部数据类型：\n'+str(df.dtypes))
print('单个数据类型：\n'+str(df.names.dtype))

#分析数据
# Create graph
df['Birth_nums'].plot()

# Maximum value in the data set
MaxValue = df['Birth_nums'].max()

# Name associated with the maximum value
MaxName = df['names'][df['Birth_nums'] == df['Birth_nums'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
print(df[df['Birth_nums'] == df['Birth_nums'].max()])
#Sorted.head(1) can also be used

plt.show()