import os
import pandas as pd
import pickle 


# Path of pkl files.
path_1 = '/Users/macbook/Desktop/Internship_PAW/code/Data/'


# Step 1 :Import the pkl files and creat 
data1= open(path_1 +'D_Operator.pkl' ,'rb')
Operator= pickle.load(data1)
#print (D_Operator)

data2 = open(path_1 +'D_Pool.pkl','rb')
Pool= pickle.load(data2)
#print(D_Pool)

data3= open(path_1 + 'D_Station.pkl','rb')
Station= pickle.load(data3)
#print(D_Station)
data4 = open(path_1 + 'D_Point.pkl','rb')
Point = pickle.load(data4)
#print(D_Point)
data5 = open(path_1 + 'MD_Dynamic.pkl','rb')
Dynamic = pickle.load(data5)
#print(D_Dynamic)


#rename the commmon column 
D_Operator = Operator.rename(columns= {'id':'operator_id'})
D_Pool= Pool.rename(columns= {'id':'pool_id','code':'pool_code','ts':'ts_pool'})
D_Station = Station.rename(columns= {'id':'station_id','ts':'ts_Station'})
D_Point  = Point.rename(columns= {'id':'point_id','code':'point_code','ts':'ts_point'})
D_Dynamic = Dynamic.rename(columns = {'code':'Dynamic_code'})

merge1=pd.merge(D_Pool,D_Operator, how='left', left_on='operator_id',right_on='operator_id')
#print(merge1)

merge2=pd.merge(merge1,D_Station, how='left', left_on='pool_id',right_on='pool_id')
#print(merge2)

merge3=pd.merge(merge2,D_Point, how='left', left_on='station_id',right_on='station_id')
#print(merge3)

merge4=pd.merge(merge3,Dynamic, how='left', left_on='point_id',right_on='point_id')

#MeraData = merge4.to_csv("W4P_Data_set.csv")

'Exploratory Analysis'
#Preparing dataset for next stage.
print('Information of data frame',merge4.info()) # additional information of dataframe
print(merge4.head()) # frist 5 rows
print(merge4.tail()) #last 5 rows
print('list all columnd names',merge4.columns) # list all columns names
print(merge4.shape) # get numbers of rows and columns
print(merge4.describe()) #statistical description, only for numeric values
