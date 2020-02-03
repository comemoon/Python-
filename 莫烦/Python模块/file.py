#写操作
test="This is my first test.\nThis is next line.\nThe last line"
append_text="\nnext line to append"
print(test)
my_file=open('myfile.txt','w')#打开,执行写操作,写到与该文件相同的文件夹下
my_file.write(test)#写内容
my_file.close()#关上

my_file=open('myfile.txt','a')#在原来基础上添加内容
my_file.write(append_text)
my_file.close()
print('#########################################')
#读操作

file0=open('myfile.txt','r')
read_text=file0.read()#读全部
print(read_text)
file=open('myfile.txt','r')
readtext2=file.readline()#读一行
readtext3=file.readline()#从原来基础上自动读下一行
readtext4=file.readlines()#读所有的行,把他们放在一个列表里
print(readtext2)
print(readtext3)
print(readtext4)
file.close()
