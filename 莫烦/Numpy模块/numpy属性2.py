import numpy as np
#First
A=np.arange(2,14).reshape(3,4)
mi=np.argmin(A)#返回最小值索引
ma=np.argmax(A)#返回最大值索引
mea=np.mean(A)#返回平均值
ave=np.average(A)#返回平均值2
median=np.median(A)#返回中位数
cum=np.cumsum(A)#返回累加和的一维矩阵
dif=np.diff(A)#返回相邻两个元素差的矩阵
zer=np.nonzero(A)#分别返回行数,列数构成的两个array
print(A)
print(mi)
print(ma)
print(mea,ave,median)
print(cum)
print(dif)
print(zer)
#Second
B=np.arange(14,-1,-1).reshape((5,3))
sor=np.sort(B)#从大到小排,从右向左排
trans=np.transpose(B)#矩阵转置
cli=np.clip(B,4,10)#保留4<x<10之间的数，其余比4小的变4，比10大的变10
print(B)
print(sor)
print(trans)
print(B.T)#矩阵转置2
print((B.T).dot(B))
print(cli)
#Third
C=np.arange(3,15).reshape(3,4)
print(C)
print(C[2,1])#索引矩阵具体的数
print(C[0:1,2:4])#输出从第0行到第1行，第2列到第4列
for row in C:
      print(row)
for row in C.T:#迭代转置
      print(row)
print(C.flatten())#将矩阵转换成一维的序列
for wit in C.flat:#flatten的迭代器
      print(wit)


