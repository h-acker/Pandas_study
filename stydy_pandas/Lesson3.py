# -*- coding : utf_8 -*-
import  pandas as pd
import  matplotlib.pyplot as plt

Location=r'E:\data_Vis\data\311_Service_Requests_from_20112.csv'
complaints=pd.read_csv(Location)

notise_complaints=complaints[complaints['Complaint Type']=='Noise - Stree/Sidewalk']

in_brooklyn=complaints['Borough']=='BROOKLYN'

#对Borugh地区噪音投诉排序
notise_complaints_count=notise_complaints['Borough'].value_counts()
complaints_count=complaints['Borough'].value_counts()
print(notise_complaints_count[:5])

rate=notise_complaints_count/complaints_count.astype(float)
rate.plot(kind='bar')

plt.show()



