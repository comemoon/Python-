import numpy as np
#First
A=np.arange(24).reshape((3,8))
array=np.split(A,2,axis=1)#将A按列分成两列,axis=1就是在行的方向上整体有4列,2:分成两部分
brray=np.split(A,3,axis=0)
crray=np.array_split(A,3,axis=1)#能进行不等分分割
drray=np.vsplit(A,3)#进行横向的分割
erray=np.hsplit(A,2)#进行纵向的分割
print(A)
print(array)
print(brray)
print(crray)
print(drray)
print(erray)
#Second
B=np.arange(4)
c=B#"="赋值相当于c的引用,B变,c也变,相互关联
d=B
e=d
B[1]=12
f=B.copy()#deep copy 改变B也不会改变f

print(c is B)#相互之间传值都是同一个,都是相互关联
print(d is B)
print(e is B)
B[2]=100
print(B)
print(c)
print(d)
print(e)
print(f)

