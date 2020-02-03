'''First One
print('hello world!')
a='hello'
print(a)
b='albert'
c=' einstein'
d=b+c
print(d)
ab=['das','des','few','qwe']
ab_1=ab[0]
ab_4=ab[-1]
#Python列表除了正向取值从0开始,
#还可以负向取值从后往前从-1,-2...以此类推
print(ab_1)
print(ab_4)
print(ab[-4])
for i in ab:
	print('hhhh'+i)
c=[]
c.append('trick')
c.append(12)
c.append('123')
print(c)

sss=[]
for i in range(1,11):#range(a,a+4) 依次返回从a 到a+3
	sss.append(i**2)
print(sss)

sqii=[i**2 for i in range(1,11)]
print(sqii)

sq3=sqii[:3]#返回前三个
print(sq3)
coppy_sq3=sqii[:]
coppy_sq3.append('23')
print(coppy_sq3)

d=(120,345)
d_1=d[0]
print(d_1)

print(1 in sqii)
print(50 not in sqii)

f={'first':334,2:456,'12':12,}
f['ty']='pp'
print(f)

for name,number in f.items():
	print(str(name)+' '+str(number))

for string in f.keys():
	print(string)
for number in f.values():
	print(number)
name =input("what do you want to say?")#默认返回字符串
print(name+'!')'''

x=1
while x<=5:
	print(x)
	x+=1
def greet_user(username='ert'):
	print('hello '+username)
greet_user('tyy')

def add_number(x,y):
	return x+y
print(add_number(3,7))

class Dog():
	"""docstring for Dog"""
	def __init__(self, name):
		self.name = name
	def sit(self):
		print(self.name+' is sitting')

my_dog =Dog('amy')

print(my_dog.name+' ggggg')
my_dog.sit()
#继承
class SARDog(Dog):
	"""docstring for SARDog"""
	def __init__(self, name):
		super().__init__(name)
	def search(self):
		print(self.name+ " is finding")
my_dog2=SARDog("Wile")

print(my_dog2.name+ " is hhhhh")
my_dog2.search()





