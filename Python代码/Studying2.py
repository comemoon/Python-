'''Users=[]
new_users={'last':'fermi',
			'first':'enrico',
			'username':'efermi',
			}
Users.append(new_users)
print(Users)
new_users={'last':'1234',
			'first':'45678',
			'username':'7890',
			}
Users.append(new_users)
print(Users)
for user_dict in Users:
	for k,v in user_dict.items():
		print(k+':'+v)
	print('\n')
fav_language={'jen':['python','rudy'],
			  'sarah':['c'],
			  'edward':['asfd','go'],
			  'phil':['oui','hasf'],
			  }
for name,lagw in fav_language.items():
	print(name+':')
	for lang in lagw:
		print('::'+lang)
users2 = {
			'aser': {
				'first' : 'asfgg',
				'last' : 'werrt',
				'location' : 'dfggh', 
			},
			'wert' : {
				'first' : 'adfef',
				'last' : 'zxcv',
				'location' : 'zxcft'
			}
}
print('\n')
for names,names_dicts in users2.items():
	print(names+':')
	for name,namr_dict in names_dicts.items():
		print(name+':'+namr_dict)
print('\n')
for names,names_dicts in users2.items():
	print(names+':')
	full_name =names_dicts['first']+' '
	full_name+=names_dicts['last']
	location = names_dicts['location']

	print('\tFull name:'+full_name.title())#title让首字母大写
	print('\tLocation:'+location.title())
#字典里的排序是没有顺序的,放入顺序跟输出顺序会不一致
#但collections板块中的OrderedDict会让字典放入与输出顺序相同
from collections import OrderedDict
fav_language= OrderedDict()#生成OrderedDict的对象
fav_language['jen']=['python','ruby']
fav_language['sarch']=['c']
fav_language['edward']=['ruby','go']
fav_language['pilh']=['python','haskell']
for name,langs in fav_language.items():
	print(name+":")
	for lan in langs:
		print('_'+lan)
aliens = []
for alien_num in range(100):
	new_alien={}
	new_alien['color']='green'
	new_alien['points']=5
	new_alien['x']=20*alien_num
	new_alien['y']=0
	aliens.append(new_alien)
num_aliens =len(aliens)
print(num_aliens)
print(aliens)'''

car = 'bmw'
print(car == 'bmw')
cd='qwe'
print(cd != car)
car ='Bmw'
print(car.lower()=='bmw')
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
if age_0 < 10:
	print("you are sure fill")
else:
	print("zzzzzzzz")

if age_0 < 10:
	print("you are sure fill")
elif age_0>1:
	print("zzzzzzzz")
else:
	print("asdfgh")
players = ['al','jk','gh','dale']
print('al' in players)
print('ala' in players)
user='wer'
if(user not in players):
	print("you are sure")
	print("======================")
players2= []
if players2:
	for play in players2:
		print(play.title())
else:
	print("We have no players yet!")

