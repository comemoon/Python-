import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)#从-3到3 50段
y1=2*x+1
y2=x**2
ticks=np.linspace(-1,2,5)

plt.figure(num=10,figsize=(8,5))#每一个plt.figure()是一个整体
l1,=plt.plot(x,y1,label='up')#返回值要加","l1, l2,
l2,=plt.plot(x,y2,color='red',linestyle='--',label='down')
plt.xlim((-1,5))#横坐标范围
plt.ylim((-2,5))#纵坐标范围
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(ticks)#可以自动控制间距
plt.yticks([-2,-1,0,1,2],
           [r'$really\ bad$',r'$bad \ \alpha$',r'$normal$',r'good',r'$really\ good$'])
            #两头加$可以变成斜体,中间\加空格才显示空格,\ \alpha 转义字符a
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')#图例

ax=plt.gca()#ax代指上面的这个图
ax.spines['right'].set_color('none')#将上右轴去掉
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#将下轴与x轴相关联
ax.yaxis.set_ticks_position('left')#将左轴与y轴相关联
ax.spines['bottom'].set_position(('data',0))#这个data处参数有好多,随后再整
ax.spines['left'].set_position(('data',0))

#添加标注
x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='g')#显示点
plt.plot([x0,x0],[y0,0],'k--',lw=2)
#方法一
plt.annotate(r'$2x+1=%s$'% y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',
                                                                   connectionstyle='arc3,rad=.2'))
#方法二
plt.text(-1.2,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',fontdict={'size':10,'color':'r'})
                                                        #两个希腊字母
#坐标轴呈现在函数之前
for label in ax.get_xticklabels()+ax.get_yticklabels():
      label.set_fontsize(12)                                #透明度
      label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))
      
plt.show()


