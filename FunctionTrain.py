import os #as ko
#as可以指定一个别名

class FunctionTrain:
    name=''
    def __init__(self,name):
        self.name=name

#file=open(,name,[])
#打开文件

file=open('KO.txt', 'r+')#读取文件还有w,w+,a,a+.‘r'是只读模式
#读取文件
print(file.read())
#写入文件
str='hello'
file.write(str)
file.close()

#with关键字可以有效防止忘记close()
with open('KO.txt', 'r+') as f:
    print("with输出的文件流:"+f.read())

#directory system
#os就是python内置的与文件操作有关的模块
print(os.name)
print(os.listdir('/'))#list all file and directory name

#os.path是对目录操作的一个python库,abspath()绝对路径
fpath=os.path.abspath(file.name)
print(fpath)
#os.path.exists()确认文件是否存在
if os.path.exists(fpath):
    print(os.path.basename(fpath))#os.path.basebane()获取文件名
    #os.rename(file.name,'Ok')

else:
    os.mkdir(fpath)#mkdir()创建文件目录
    os.rename(file.name, 'KO')

#os.stat()可以获取文件的信息
fileinfomation=os.stat(fpath)
print(fileinfomation.st_mode)#st_mode文件是否可读
print(fileinfomation.st_size)#st_size文件大小
print(fileinfomation.st_atime)
print(fileinfomation.st_ctime)



