import  pandas as pd
import  matplotlib.pyplot as plt
import  numpy as np

Location=r'E:\data_Vis\data\311_Service_Requests_from_2011.csv'
complaints=pd.read_csv(Location)
print(complaints['Complaint Type'][:5])

complaint_counts=complaints['Complaint Type'].value_counts()[:10]
print(complaint_counts)

complaint_counts.plot(kind='bar')
plt.show()
