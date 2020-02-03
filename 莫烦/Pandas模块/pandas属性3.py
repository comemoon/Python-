import numpy as np
import pandas as pd
#First
dates=pd.date_range('20200101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[2,3]=np.nan
print(df)

print(df.dropna(axis=0,how='any'))#axis=0表示丢掉某一行,1表示丢掉某一列
                                    #how='any' 表示只要有nan就丢,all表示一行都是nan才丢掉

print(df.fillna(value=100))#把所有nan都改成100

print(df.isna())#有nan返回True
print(np.any(df.isnull())==True)#只要有一个nan就返回True
print(np.all(df.isnull())==True)#全部为nan才返回False


