import numpy as np
import pandas as pd
#First

#$concaing
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)  
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True) #axis=0 进行纵向合并#ignore_index=True 忽略之前行的序列号,重新排序                                
res2=pd.concat([df1,df2,df3],axis=1) #axis=1 进行横向合并
print(res)
print(res2)

##join
df4=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df5=pd.DataFrame(np.ones((3,4))*1,columns=['c','d','e','f'],index=[3,4,5])
print(df4)
print(df5) #concat只能把行名称相同或列名称相同进行合并,不相同的用nan代替
pca=pd.concat([df4,df5],axis=1)
print(pca)
pca2=pd.concat([df4,df5],axis=0,join='inner',ignore_index=True)#只保留相同的部分
print(pca2)

##join_axes
pca3=pd.concat([df4,df5],axis=1,join_axes=[df4.index])
print(pca3)                   #join_axes=[df4.index]以df4.index格式进行扩充
pca4=pd.concat([df4,df5],axis=1,join_axes=[df5.index])
print(pca4)

##append
df7=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df8=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df9=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
asd=df7.append([df8,df9],ignore_index=True)
print(asd)
asd2=asd.append(s1,ignore_index=True)#append 添加方式
print(s1)
print(asd2)



