import pandas as pd
import numpy as np
#读取数据
datas=pd.read_csv('2015.csv')#数据文件要跟此文件放在同一文件夹下才可调用
datas2=pd.read_csv('data.csv')
print(datas)
print(datas2)
#存储数据
datas.to_pickle('excel2015.pickle')
#合并DaeFrame
