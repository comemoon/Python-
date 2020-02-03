import pickle 
# pickle 保存数据
a_dict={'da':111,2:[23,1,3],'23':{1:2,'d':'sad'}}
file=open('example.pickle','wb')
pickle.dump(a_dict,file)
file.close()
#读pickle文件
file2=open('example.pickle','rb')
adict=pickle.load(file2)
file2.close()
print(adict)
with open('example.pickle','rb') as file3:#简化版本,会自动关闭
     adict=pickle.load(file3)
print(adict)
