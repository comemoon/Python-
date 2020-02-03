'''
#Lists
users=['val','bob','bat','rty'] #列表中括号
user_1=users[0]
user_2=users[1]
user_last=users[-1]
print(user_1)
print(user_2)
print(user_last)
users[0]='wwwwww'
users[-2]='rrrrr'
print(users)
users.append('amy')
print(users)
users.insert(0,'joe')
users.insert(3,'bre')
print(users)
del users[-1]
print(users)
users.remove('joe')
print(users)
try_pop=users.pop()#列表是堆结构,后进先出,pop()取出的是最后一个
print(try_pop)
try_pop2=users.pop(2)
print(try_pop2)
print(users)
num_users=len(users)
print(str(num_users)+" items")
users.sort()#默认从小到大
print(users)
users.sort(reverse=True)#从大导到小排
print(users)
print(sorted(users))
print(sorted(users,reverse=True))
for i in users:
	print(i)
for number in range(101):#从0 to 100
	print(number)
for number2 in range(1,101):#从 1 to 100
	print(number2)
number_list = list(range(1,1001))
print(number_list)
ages=[72,43,56,78,243,2]
min_age=min(ages)
print(min_age)
max_age=max(ages)
print(max_age)
finershers=['vbg','bhy','kai','age','frg','qwe','iop']
first_tree=finershers[:3]
print(first_tree)
seconf=finershers[1:3]
print(seconf)
lasttree=finershers[-3:-1]
print(lasttree)
copy_list =finershers[:]#copy成两个
copy2_list=finershers#原列表多了个名字而已,改它原列表也变
copy_list.append('1213')
copy2_list.append('6780')
print(finershers)
print(copy2_list)
print(copy_list)
squares=[]
for x in range(1,11):
	sqire=x**2
	squares.append(sqire)
print(squares)

squares2=[x**2 for x in range(1,11)]
print(squares2)
names=['tyu','qwe','yui','rfb']
upper_names=[]
for name in names:
	upper_names.append(name.upper())#小写变大写
print(upper_names)

upper_names2=[name.upper() for name in names]
print(upper_names2)

dimensions = (800,609)

for e in dimensions:
	print(e)
print(dimensions)
dogs = []
dogs.append('while')
dogs.append('qwe')
dogs.append('asd')
dogs.append('fsa')

for dog in dogs:
	print('hello '+dog)
old_dogs = dogs[:2]
for old_dog in old_dogs:
	print(old_dog)
del dogs[0]
dogs.remove('fsa')
print(dogs)'''

#Dictionaries
alien_0 ={'color':'green','prints':5}
print(alien_0['color'])
print(alien_0['prints'])

alien_0 ={'color':'green'}
alien_color = alien_0.get('color')
print(alien_color)
alien_points= alien_0.get('prints',0)#如果指定的键不存在,返回none,也可以指定参数返回
print(alien_points)
print(alien_0)
art={'color':'green','prints':5}
art['x']=0
art['y']=25
art['sqwe']=1.5
print(art)

art={'color':'green','prints':5}
art['color']='yellow'
print(art)
del art['prints']
print(art)

fav_languages={ 'jen':'python',
				'sarch':'c',
				'edar':'ref',
				'pjll':'asd',
				}
for name,languaf in fav_languages.items():
	print(name+':'+languaf)
for name in fav_languages.keys():
	print(name)
for qwe in fav_languages.values():
	print(qwe)

for name in sorted(fav_languages.keys()):
	print(name+":"+fav_languages[name])
numlen = len(fav_languages)
print(numlen)


