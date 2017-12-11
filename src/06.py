#类和实例
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_name(self):
        print('%s:%s'%(self.name,self.age))
bart=Student('dantyli',21)
bart.print_name()
#内部属性不被外部访问,名称前加__,变成私有变量
class Student1():
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score():
        print('%s:%s'%(self.__name,self.__score))
    def get_name(self):
        return self.__name
bar=Student1('dantyli',50)
#bar.__name,外部代码访问需要增加方法
print(bar.get_name())
class Person():
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender!='male' and gender!='female':
            raise ValueError('bad value')
        else :
            self.__gender=gender
p=Person('tommy','male')
print(p.get_gender())
p.set_gender('female')
print(p.get_gender())
#继承,多态
print(isinstance(p,Student))
class Animal():
    def run():
       print('Animal is running')
class Dog(Animal):
    def run():
       print( 'Dog is running')
class Cat(Animal):
    def run():
       print( 'Cat is running')
Dog.run()
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Cat)
#获取对象信息type,dir获取一个目标的所有属性和方法
#print(type(123))
#print(dir('123'))
#hasattr,setattr,getattr
class worker():
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
we=worker()
print(hasattr(we,'x'))
setattr(we,'x',10)
print(getattr(we,'x'))
#实例属性和类属性名字相同实例会覆盖掉类的内容
#使用__slots__
class Student2():
    __slots__=('name','age')#用tuple定义可以绑定的属性名称
s=Student2()
s.name='dantyli'
print(s.name)
#s.score=90 子类允许定义的属性是子类的__slots__加上父类的__slots__
#@property装饰器,将方法转化为属性调用
class Student3():
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score is int')
        else :
            if 0 <= value <=100:
                self.__score=value
ss=Student3()
#ss.score='hi'
#ss.score=1002
ss.score=80
print(ss.score)
#getter只读属性
class Student5():
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        self.__birth=value
    @property
    def age(self):
        return 2017-self.__birth
s=Student5()
s.birth=2011
print(s.age)
