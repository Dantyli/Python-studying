 #多重继承
class Animal(object):
    pass
class Runnable(object):
    def run(self):
        print('Running ...')
class Dog(Animal,Runnable):
    pass
#MixIn
class RunnableMixIn(object):
    def run(self):
        print('Running ...')
class Dog(Animal,RunnableMixIn):
    pass
#__str__
class Student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name:%s)'%self.name
print(Student('dantyli'))
#文件
with open('dantyli.txt') as file_object:
    contents=file_object.read()
#    print(contents)
with open('dantyli.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
#使用文件内容
filename='dantyli.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
strin=''
for line in lines:
    strin += line.rstrip()
#number=input('please enter your luckly number')
print(strin)
#写入文件
with open(filename,'w') as file_object:
    file_object.write('i love programming')
#附加到文件
with open(filename,'a') as file_object:
    file_object.write('i am dantyli')
#异常try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by zero')
#__getitem__
class Fib():
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
#判断切片对象
class Fib():
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for n in range(n):
                a,b=b,a+b
            return a
        if isinstance (n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a,b=b,a+b
            return L
f=Fib()
print(f[0:10])
#__getattr__调用不存在的属性时
class Student():
    def __init__(self,name):
        self.name=name
    def __getattr__(self,attr):
        if attr=='score':
            return 100

s=Student('dantyli')
print(s.score)
#链式调用
class Chain():
    def __init__(self,path=''):
        self.__path=path
    def __getattr__(self,path):
        return Chain('%s%s'%(self.__path,path))
    def __str__(self):
        return self.__path
    __repr__=__str__
print(Chain().status.user.timeline.list)
#调用实例的方法
class Student():
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s' % self.name)
ss=Student('tom')
ss()
#callable()函数判断一个对象是否可调用
print(callable(ss))
