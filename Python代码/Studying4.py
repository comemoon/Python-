'''from Studying3 import Car

class Battery():
	def __init__(self,size=70):
		self.size=size
		self.charge_level=0
	def get_range(self):
		if self.size == 70:
			return 240
		elif self.size == 85:
			return 279

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()#类的组合
	def charge(self):
		self.battery.charge_level=85
		print('The vehicle is fully charged!')
	def fill_tank(self):#父类方法重写
		print("Tis car has no fuel tank")

myaaaa=ElectricCar('tessa','mofre',2016)
myaaaa.charge()
print(myaaaa.battery.get_range())
myaaaa.drive()

class ClassName(object):
class Car(object):
class ChildClassName(ParentClass):
	def __init__(self):
		super(ClassName,self).__init__()

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super(ElectricCar,self).__init__(make,model,year)'''
'''
#在列表里面添加对象
gas_fleet=[]
electric_fleet=[]
for _ in range(500):
	car = Car('ford','fource',2019)
	gas_fleet.append(car)
for _ in range(250):
	ecar = ElectricCar('asd','ghj',2013)
	electric_fleet.append(ecar)
for car in gas_fleet:
	car.fill_tank()
for ecar in electric_fleet:
	ecar.charge()
print(len(gas_fleet))
print(len(electric_fleet))'''
'''
filename = 'aaaa.txt'
with open(filename) as f_obj:
	contents= f_obj.read()
print(contents)

filename = 'aaaa.txt'
with open(filename) as f_obj:
	for line in f_obj:
		print(line.rstrip())

filename='aaaa.txt'
with open(filename) as f_obj:
	lines=f_obj.readlines()
for line in lines:
	print(line.rstrip())

filename = 'bbbb.txt'
with open(filename,'w') as f:
	f.write("I love programing!")
filename = 'bbbb.txt'
with open(filename,'a') as f:
	f.write("\nI love programing!")
	f.write('\nI love making files')
try:
	print(5/0)
except ZeroDivisionError:
	print("Error!")
f_name ='bbbbaa.txt'
try:
	with open(f_name) as f_obj:
		lines = f_obj.readlines()
except FileNotFoundError:		
	msg = 'Cant not find file {0}.'.format(f_name)
	print(msg)
#format函数 
#"{0} {1}".format("hello", "world")  # 设置指定位置
#'hello world'

f_names =['aaaa.txt','siddhartha.txt',
'moby_dick.txt','bbbb.txt']
for f_name in f_names:
	try:
		with open(f_name) as f_obj:
			lines = f_obj.readlines()
	except FileNotFoundError:
		pass#异常处不能啥都不写,pass :不做任何事情，只起到占位的作用
	else:#else是与except同层,没有异常发生时，else中的语句将会被执行。
		num_lines = len(lines)
		msg = '{0} has {1} lines.'.format(f_name,num_lines)
		print(msg)
try:
	pass
except Exception as e:
	print(e,type(e))

import json

numbers=[2,3,4,5,6,8]

filename = 'number.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj) 

f_name = 'number.json'

try:
	with open(f_name) as f_obj:
		numbers = json.load(f_obj)
except FileNotFoundError:
	msg = "Cant find {0}.".format(f_name)
	print(msg)
else:
	print(numbers)'''
'''
from full_names import get_full_name
janis = get_full_name('aaaa','bbbb')
print(janis)

bob = get_full_name("assaa","tttt")
print(bob)'''
'''
#单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
#先写一个类,必须继承unittest.TestCase方法，
#用例(测试方法)用test开头，否则不识别！
assertEqual(a,b,msg="None")  判断a,b是否相等，不相等时，抛出msg；
assertTure(x,msg="None") 判断x表达式是否为真，表达式为假时，抛出msg；
assertIn(a,b,msg="None") 判断a是否在b里面，a不在b里面时，抛出msg；
assertIsNone(x,msg="None") 判断x是否为空，x不为空时，抛出msg。
#调用unittset.main()方法运行测试用例
'''

'''import unittest 
from full_names import get_full_name
class NamesTestCase(unittest.TestCase):
	def test_first_last(self):
		full_name=get_full_name('Z','q')
		self.assertEqual(full_name,'Z Q','错误')
	def test_middle(self):
		full_name=get_full_name('da','asd','jk')
		self.assertEqual(full_name,'Da Jk Asd')
unittest.main()
class QW(unittest.TestCase):
	
	def test(self):
		#self.assertEqual(1,2)
		self.assertNotEqual(1,2)
unittest.main()'''

import unittest
from full_names import Accountant

class TestAccountant(unittest.TestCase):
#setUp函数：初始化环境
#（执行每条用例之前，都要执行setUp函数下面的代码，每次都要执行）
	def setUp(self):
		self.acc=Accountant()
	def test_INITIAL_BALANCE(self):
		acc=Accountant()
		self.assertEqual(acc.balance,0)
		acc=Accountant(100)
		self.assertEqual(acc.balance,100)
	def test_deposit(self):
		self.acc.deposit(100)
		self.assertEqual(self.acc.balance,100)
		self.acc.deposit(100)
		self.acc.deposit(100)
		self.assertEqual(self.acc.balance,300)
	def test_withdrawal(self):
		self.acc.deposit(1000)
		self.acc.withdraw(100)
		self.assertEqual(self.acc.balance,900)
unittest.main()


unittest.main()




	
		

		

