XPPLE=10012
def ill():
      print("This is a function")
      a=1+2
      print(a)
ill()
def fun(a,b):
      c=a*b
      print('this is ',c)
fun(1,5)
fun(a=1,b=5)
def sale_car(price,color='blue',brand='carmy',is_second=True):
      print('price',price,
            'color',color,
            'brand',brand,
            'is_second',is_second)
sale_car(1000,'red')
def fun():
      
      a=10
      print(a)
      print(XPPLE)
      return a+100
fun()
print(fun())

#global
a=None
def pin():
      global a
      a=20#在函数内部变成全局变量,1.需要在外none,2,需要在函数内部声明,赋值,3,运行函数
      return a+100
print(a)
print(pin())
print(a)
      
