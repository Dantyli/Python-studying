#求解一元二次方程,定义函数
import math
def quadratic(a,b,c):
        if b*b>4*a*c:
                return (-b+math.sqrt(b*b-4*a*c))/(2*a)
        else:
                raise TypeError('该函数无解')
#print(quadratic(1,3,1))
#函数参数
def power(x,n):
        s=1
        while n>0:
                n=n-1
                s=s*x
        return s
#print(power(3,3))
#默认参数
def enroll(name,gender,age='5',city='shenzhen'):
        print('name',name)
        print('gender',gender)
        print('age',age)
        print('city',city)
#enroll('dantyli','male')
def add_end(L=[]):
        L.append('END')
        return L
#print(add_end([1,2,3]))
#print(add_end())
#print(add_end())
#默认参数必须指向不变对象
def add_end(L=None):
        if L is None:
                L=[]
        L.append('END')
        return L
#print(add_end())
#print(add_end())
#定义可变参数
def calc(*numbers):
        sum=0
        for n in numbers:
                sum=sum+n*n
        return sum
#print(calc(1,3))
nums=[1,2,3]
#print(calc(*nums))
#*nums 表示把nums list 中的所有元素作为可变参数传进去
rang=range(1,10)
#print(list(rang))

for id in range(1,10):
       # print(id)
        if id==5:
                break
r=list(range(1,10))
s=[1,2,'dantyli','lice','hello']
#s.reverse() #此为操作
#print(s[:2])切片
#print(s[:])
name='dantyliislice'
#print(name[:5])
def trim(s):
        if(len(s)==0 or (s[1]!=''and s[-1]!='')):
                return s
        elif s[1]=='':
                return s[1:]
        elif s[-1]=='':
                return s[-1:]
#print(len(trim('dantyli ')),len('dantyli '))
#print(name[::2])
#for i,v in enumerate(s):
        #print(i,v)
#是否可以迭代       
from collections import Iterable
#print(isinstance(123,Iterable))
def getMn(nums):
        if(isinstance(nums,Iterable)):
                max=nums[0]
                min=nums[0]
                for num in nums:
                        if num>max:
                                max=num
                        if num<min:
                                min=num
                return min,max
        else:
                return nums
#print(getMn([1,5,2,1,4,8]))
#列表生成时把x*x写在前面
#print([x*x for x in range(1,11)if x%2==0])
#生成全排列
all=[m+n for m in 'abc'for n in 'xyz']
#print(all)
d={'a':'alice','b':'bob','c':'cony','d':'dantyli'}
#for k,v in d.items():
        #print(k,'=',v)
ss=['qwe','fasdf']
s=[s.title() for s in ss]
print(s)
