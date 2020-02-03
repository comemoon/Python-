import numpy as np
import pandas as pd

left=pd.DataFrame({'key':['K0','K1','K2','K3'],#一列一列的生成
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K100','K2','K3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']})
print(left)
print(right)
res=pd.merge(left,right,on='key')#保留相同key列,并除去key中不同值的那一行
print(res)

left=pd.DataFrame({'key':['K0','K0','K1','K1'],#一列一列的生成
                   'key2':['K4','K5','K9','K7'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K100','K2','K3'],
                     'key2':['K4','K5','K6','K7'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']})
print(left)
print(right)
                  #how=[inner(默认),outer,left,right]   #outer全部包括 left,right 按单方面看
res2=pd.merge(left,right,on=['key','key2'],how='inner')#inner保留key,key2同时相同的
print(res2)

res3=pd.merge(left,right,on='key',how='outer',indicator='Find')#可以改名字
print(res3)                               #告诉你是哪部分的数据



left=pd.DataFrame({ 'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']},
                  index=[1,2,3,5])
right=pd.DataFrame({'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']},
                   index=[2,3,4,6])
print(left)
print(right)
req=pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(req)

boys=pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['k0','k0','k3'],'age':[4,5,6]})
print(boys)
print(girls)        
res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)
