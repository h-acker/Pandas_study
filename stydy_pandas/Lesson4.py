#-*- coding: utf_8 -*-
import pandas as pd
from numpy import  random
import numpy as np
import matplotlib.pyplot as plt
import  matplotlib
import sys

names=['Bob','Jes','Mary','Jhon','Mel']

random.seed(500)

random_names=[names[random.randint(low=0,high=len(names))] for i in range(1000)]
births=[random.randint(low=0,high=1000) for i in range(1000)]
BabyBirthData=list(zip(random_names,births))
df=pd.DataFrame(data=BabyBirthData,columns=['Names','Births'])
#print(df.info())
df.to_csv('Births2017.txt',index=False,header=['Names','Birthnums'])

Location=r'E:\data_Vis\code\stydy_pandas\Births2017.txt'
df=pd.read_csv(Location)
name=df['Names'].unique()
name_num=df.groupby('Names').sum()
Sorts=name_num.sort_values(['Birthnums'],ascending=False)
print(Sorts.head(1))

Sorts.plot(kind='bar')
plt.show()