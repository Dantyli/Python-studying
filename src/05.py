#返回函数
def calc_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=calc_sum(1,3,5,2,4)
print(f())
#闭包
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))#f(i)立即被执行,因此i的当前值传入f()
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())
#nonlocal使内层函数可以修改外层函数的变量
def c():
    n=0
    def counter():
        nonlocal n
        n+=1
        return n
    return counter
c1=c()
#print(c1(),c1(),c1())
#匿名函数lambda
l=list(map(lambda x:x*x ,[1,2,3,4,5]))
print(l)
l=list(filter(lambda x:x%2==1,range(1,10)))
#装饰器decorator 返回函数的高阶函数
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2017-12-05')
now()
#@log放到函数定义处,相当于执行了now=log(now)
#偏函数
import functools
int2=functools.partial(int,base=2)
print(int2('10000'))
#类class
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+' now is sitting.')
    def roll_over(self):
        print(self.name.title()+' now is rolling')
#实例化
my_dog=Dog('bob',5)
my_dog.sit()
my_dog.roll_over()
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')
    #通过方法修改属性的值
    def update_odometer(self,mileage):
        self.odometer_reading=mileage
my_new_car=Car('audi','a8',2016)
print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading=10
my_new_car.update_odometer(100)
my_new_car.read_odometer()
#继承super关联子类与父类
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
my_tesla=ElectricCar('tesla','model s',2017)
n=my_tesla.get_descriptive_name()
print(n)

    
