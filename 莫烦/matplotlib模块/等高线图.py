import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
      return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n=256
x=np.linspace(-3,3,n)#生成-3到3连续的256个点
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)
#整体圈圈设置                        #整体是hot颜色
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#等高线设置
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=0.5)
                        #划分成8个层次,会有8个圈
#线上数字标注
plt.clabel(C,inline=True,fontsize=10)
            #写在线里面  字体大小


plt.xticks(())#将x,y坐标轴隐藏
plt.yticks(())

plt.show()
