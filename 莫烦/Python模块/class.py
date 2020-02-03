class Calculator:
      name='Good calculator'
      price=18
      def __init__(self,name,price,hight=123,width=789):#构造函数,固定名字
            self.name=name
            self.price=price
            self.hight=hight
            self.width=width
      def add(self,x,y):#类中函数形参必须带 self 就代指自己
            result=x+y
            print(result)
      def minus(self,x,y):
            result=x-y
            print(result)
      def times(self,x,y):
            print(x*y)
      def divide(self,x,y):
            print(x/y)

calcu=Calculator('qwe',123)
print(calcu.hight)
print(calcu.name)
calcu.add(1,3)
calcu.minus(12,56)
            
