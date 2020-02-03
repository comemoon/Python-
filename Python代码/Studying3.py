'''
def greet_user():
	print("Hello!")
greet_user()

def greet_and(username):
	print('hello'+username+'!')
greet_and("hasfesa")
greet_and("qwer")

def desxribe_pet(animal,name):
	print('I have a '+ animal+'.')
	print('It is your '+name+'!')
desxribe_pet(animal='pig',name='anird')
desxribe_pet(name='pig',animal='anird')
desxribe_pet('pig','anird')

def desxribe_pet2(animal,name='dogg'):#第一个形参不能带值,只能第二个带
	print('I have a '+ animal+'.')
	print('It is your '+name+'!')
print('\n')
desxribe_pet2(animal='pig',name='anird')
desxribe_pet2('anird')
desxribe_pet2('pig','anird')

def desxribe_pet2(animal,name=None):#第一个形参不能带值,只能第二个带
	print('I have a '+ animal+'.')
	if name:#如果name不是none才输出
		print('It is your '+name+'!')
print('\n')
desxribe_pet2(animal='pig',name='anird')
desxribe_pet2('anird')
desxribe_pet2('pig','anird')


def get_fullname(first,last):
	full_name=first+' '+last
	return full_name.title()
musician=get_fullname('tyu','rty')
print(musician)


def build_person(first,last):
	persion={'first':first,'last':last}
	return persion
musician=build_person('jimi','hendrix')
print(musician)

def build_person(first,last,age=None):
	persion={'first':first,'last':last}
	if age:
		persion['age']=age
	return persion
musician=build_person('jimi','hendrix',25)
print(musician)

musician=build_person('jimi','hendrix')
print(musician)

def greet_users(names):#形参是列表
	for name in names:
		msg= name+' !'
		print(msg)
username=['qwer','fdedg','hrdeds']
greet_users(username)
'''
'''
Python参数传递采用'传对象引用'方式:
  函数收到的是一个可变的对像(字典或者列表)的引用,能修改对象的原始值----传引用
  函数收到的是一个不可变对象(数字元组或者字符)的引用,不能直接修改原始对象----传值

'''
'''
def print_models(unprinted,printed):
	while unprinted:
		current_model =unprinted.pop()
		print('Printing'+current_model)
		printed.append(current_model)
unprinted =['assf','wetw','tyuuii']
printed=[]
print_models(unprinted,printed)
print("\nUnprinted:",unprinted)
print("Print:",printed)

def print_models(unprinted,printed):
	while unprinted:
		current_model=unprinted.pop()
		print(current_model)
		printed.append(current_model)
original =['phone','pendA','ring']
printed=[]
print_models(original[:],printed)
print(original)
print(printed)
#*toppings 叫做可变参数,可传任意数量的参数,toppings接受的是一个元组,
def make_pizza(size,*toppings):
	print(size+" ")
	for topp in toppings:
		print('-'+topp)
print('\n')
make_pizza('small','pepperoni')
make_pizza('small','pep','oppppa')
make_pizza('small','pepperoni','rttyyyu','hgfd','juyffd')
# **users 以字典的形式导入,导入多少个都行 形式:location='princent' 
def aaaaa(first,last,**users):
	profile={'first':first,'second':last}
	for key,value in users.items():
		profile[key]=value
	return profile
user_0 = aaaaa('albert','esitein',location='princent')
user_1 = aaaaa('gdth','cyuiio',location='paity',field='chemisty')
print(user_0)
print(user_1)

import pizza
pizza.make_pizza('medium','asfsdfsa')
pizza.make_pizza('qewqdsa','zcv','itfy')

from pizza import make_pizza
make_pizza('medium','asfsdfsa')
make_pizza('qewqdsa','zcv','itfy')

import pizza as p
p.make_pizza('medium','asfsdfsa')
p.make_pizza('qewqdsa','zcv','itfy')

from pizza import *
make_pizza('medium','asfsdfsa')
make_pizza('qewqdsa','zcv','itfy')'''

class Car():
	def __init__(self,make,modal,year):
		self.make=make
		self.modal=modal
		self.year=year

		self.fuel_capacity=15
		self.level=0

	def fill_tank(self):
		self.level =self.fuel_capacity
		print('Good')
	def drive(self):
		print('The car is moving')
	def update_fuel_level(self,new_level):
		if new_level <=self.fuel_capacity:
			self.level=new_level
		else:
			print('ok')
	def add_fuel(self,amount):
		if(self.level+amount<=self.fuel_capacity):
			self.level+=amount
			print('Add_frg')
		else:
			print('qwertyu')
'''my_car=Car('audi','a4',2016)
print(my_car.make)
print(my_car.modal)
print(my_car.year)

my_car.fill_tank()
my_car.drive()

ok_car=Car('yui','r4',2016)
ok_car.level=5'''
#继承的形式,继承变量跟方法(除构造方法)
class ElectricCar(Car):
	def __init__(self,make,model,year):
		#利用父类构造函数初始化
		super().__init__(make,model,year)
		self.battery_size=70
		self.charge_level=0
	def  charge(self):
		self.charge_level=100
		print("Zxcvgbhnjk")
'''myew_car=ElectricCar('tesla','model s',2016)

myew_car.charge()
myew_car.drive()'''




