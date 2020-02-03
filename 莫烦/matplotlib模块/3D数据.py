import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mpd

fig= plt.figure()
ax=mpd.Axes3D(fig)

X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)             #行跨度 列跨度
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
      #底面样子,压到z轴   比0轴低两个
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)
plt.xticks(())
plt.yticks(())
plt.show()
