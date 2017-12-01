#map和reduce
def f(x):
    return x*x
r=map(f,[1,2,3,4,5])
print(list(r))
from functools import reduce
def fn(x,y):
    return x*10+y
l=reduce(fn,[1,3,5,7,8,9])
#str转换int的方法
def strint(s):
    def fn(x,y):
        return x*10+y
    def charnum(s):
        return  {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(charnum,s))
def foo(s):
    c=s.lower()
    return c.title()
d=map(foo,['DDD','aAa','TtT'])
def prop(s,z):
    return s*z
d=reduce(prop,[1,5,2,4])
#filter
def filter_odd(s):
    if s%2==0:
        return s
l=filter(filter_odd,[1,2,3,4,5,6,7,8])
#删除空字符串
def not_empty(s):
    return s and s.strip()
p=list(filter(not_empty,['a','','b',None,' ']))
#求素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x : x % n > 0
def primes():
    yield 2
    it=_odd_iter() #初始序列
    while True:
        n=next(it) #返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)#构造新的序列
#打印100以内的素数
for n in primes():
    if n < 100:
        print(n)
    else :
        break
#切片实现回数[::-1]
def is_nums(n):
    return str(n)==str(n)[::-1]
p=filter(is_nums,range(1,1000))
#sorted排序
f=[1,3,4,2,5,3,9]
print(sorted(f,reverse=True))
L=[('Bob',85),('Adam',90),('Tony',66),('Dantyli',90)]
def by_name(t):
    return t[0].lower()
print(sorted(L,key=by_name))
#字典
f_languages={
    'lice':['javascript','python'],
    'dantyli':['java','php'],
    'bob':['perl','swift']
    }
for name,languages in f_languages.items():
    print("\n"+name.title()+"'s favorite languages are :")
    for language in languages :
        print("\t"+language.title())
#input()
message=input('Please tell your name :')
print("Hello, "+message)
#使用int()获取数值输入
age=input('How old are you ?')
age=int(age)
if age > 18 :
    print('\n You are a adult')
