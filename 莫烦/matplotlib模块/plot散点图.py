import matplotlib.pyplot as plt
import numpy as np

plt.figure()
n=1024
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)#颜色生成
plt.scatter(X,Y,s=15,c=T,alpha=0.5)
             # 点大小 颜色  透明度
plt.scatter(np.arange(5),np.arange(5))
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())#隐藏x,y坐标数值
plt.yticks(())

plt.figure()
plt.scatter(np.arange(5),np.arange(5))
plt.show()
