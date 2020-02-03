import numpy as np

#First
array=np.array([[[1,2,3]]]) #把一个列表转换成矩阵
print(array)
print(array.ndim)#返回维数,[]的个数就是维数
print(array.shape)#返回行数,列数
print(array.size)#返回元素个数
#Second
brray=np.array([2,23,4],dtype=np.float)#定义数据的类型
print(brray.dtype)#返回数据类型
print(brray)
print(brray.ndim)
#Third
crray=np.zeros((3,4)) #生成全0的矩阵,输入一个shape
drray=np.ones((5,6),dtype=np.int16)
erray=np.empty((3,5))#几乎为零
farray=np.arange(1,12,5)#开头,结尾,步距
garray=np.arange(12).reshape(3,4)#生成三行四列矩阵
harray=np.linspace(1,10,5)#生成1维线段 5个元素,从1到10依次递增
iarray=np.linspace(1,12,6).reshape(2,3)
warray=np.linspace(1,13,9).reshape(3,3)
print(drray)
print(erray)
print(farray)
print(garray)
print(harray)
print(iarray)
#Fourth
krray=crray-garray#矩阵相减 print(krray) urray=np.arange(4) print(urray**2)
trray=np.zeros((2,3))
trray=np.cos(trray) #是对矩阵中每一个值进行cos
print(trray)
print(krray<2)#返回一个矩阵,矩阵每个值为都进行判断,返回True或者False
#c=iarray*warray  逐个相乘
#print(c)
c_dot=np.dot(iarray,warray)  #矩阵乘法
c_dot_2=iarray.dot(warray)    #矩阵乘法2
print(c_dot_2)
print(c_dot)
trr_ran=10*np.random.random((2,4))
print(trr_ran)
print(np.sum(trr_ran))#返回矩阵元素和
print(np.min(trr_ran,axis=0))#返回最小值
print(np.max(trr_ran,axis=1))#返回最大值
                        #axis=0,每一列;axis=1,每一行



