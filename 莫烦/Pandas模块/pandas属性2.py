import numpy as np
import pandas as pd
#First
dates=pd.date_range('20200101',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
df2=df[0:4]
print(df)
print(df2)
print(df['a'])#返回指定某一列
print(df.b)#返回指定某一列
print(df[0:4]) #返回指定某列
print(df['20200103':'20200105'])

print(df.loc['20200104']) #以标签形式返回指定行数
print(df.loc[:,['a','d']])#返回指定列
print(df.loc['20200104','c'])#利用标签返回具体某一值

print(df.iloc[3]) #利用序列号返回某一行
print(df.iloc[2:3,1:2])#序列号返回指定切片
print(df.iloc[[1,3,5],[1,3]])#序列号可以不连续的筛选
print(df.iloc[3,2])#序列号返回具体某一值

#print(df.ix[:3,['a','c']])#ix 利用序列号跟标签混合筛选
print(df)
print(df[df.a>8])#返回a列比8大的行

#Second
df.iloc[3,2]=100#改变具体某值
df.loc['20200101','d']=200
df.a[df.b>10]=300#指定某一列改变
print(df)
df[df.b>10]=300#将b列大于10的所有行中元素变为300
print(df)
df['f']=np.nan#重新定义新的一行
df['e']=pd.Series([1,2,3,4,5,6],index=dates)#规定好行列的名称
print(df)


