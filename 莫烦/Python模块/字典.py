#字典 没有顺序
dic={'apple':1,'pear':2,'orange':3}
dic2={1:'a','c':'b'}
print(dic['apple'],dic2[1])
del dic['pear']
print(dic)
dic['cc']=12
print(dic)
def fun():
      print('123')
dic3={1:[1,2,3],'tre':{'4':3,1:'a'},'orange':fun}#字典放啥都行,用键值对<key,value>
print(dic3[1][0])
