ex_list=['a','b','c','c','d','d','d']
print(set(ex_list))#去除重复元素,会乱序
sence='qwasdasdzxccde'
print(set(sence))
ex2=set(ex_list)
ex2.add('x')#加重复的会自动删去
print(ex2.remove('x'))#如果除去的本身不存在,会报错
print(ex2.discard('oo'))#跟remove相同,但不会报错,会返回原列表
print(ex2)
ex3={'a','c','r','k'}
print(ex2.difference(ex3))#返回ex2里不与ex3重叠的部分
print(ex2.intersection(ex3))#返回两者相交的部分
