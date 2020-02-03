import pandas as pd
import numpy as np

#First
s=pd.Series([1,3,6,np.nan,44,1])#nan==>null,一个序列
print(s)
dates=pd.date_range('20200101',periods=6)#生成了日期序列,范围6个
print(dates)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df) #index 行 columns 列,自己规定行跟列名称
df2=pd.DataFrame(np.arange(12).reshape((4,3))) #自动规定行跟列名称
print(df2)
df3=pd.DataFrame({'A':1.,
                  'B':'fool',
                  'C':pd.date_range('20200101',periods=4),
                  'D':pd.Categorical(["test","try","case","fu"]),
                  'E':pd.Timestamp('20000101')},index=['a','b','c','d'])
                  #自己规定内容
print(df3)
print(df3.dtypes)#返回每一列数据类型
print(df3.index)#返回行的名称序列
print(df3.columns)#返回列得序列名称
print(df3.values)
df4=df2.describe()#返回每一列的平均值,方差,最大值,最小值等等...
print(df4)
print(df4.T)#转置
df5=df2.sort_index(axis=1,ascending=False)#ascending False从大到小排序,True 从小到大排序
                        #axis=1 把列的序号进行排序
print(df2)
print(df5)
df6=df3.sort_values(by='D')#以'D'列进行排序
print(df6)



