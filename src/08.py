#枚举类
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
#type()函数既可以返回一个对象的类型,又可以创建出新的类型
class Hello():
    def hello(self,name='world'):
        print('Hello %s .'% name)
h=Hello()
#h.hello()
print(type(Hello))
#动态创建class
def fn(self,name='dantyli'): #先定义函数
    print('Hello %s'% name)
Hello=type('Hello',(object,),dict(hello=fn))#创建Hello class
h=Hello()
h.hello()
#错误处理,try...except跨越多层调用
try:
    print('try...')
    r=10/0
    print('result',r)
except ZeroDivisionError as e:
    print('except',e)
else:
    print('finally...')

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error',e)

#使用异常避免崩溃else
print('Give me two numbers ,and i will divide them')
print("enter 'q' to quit")
while True:
    first_num=input('\n first number')
    if first_num=='q':
        break
    second_num=input('\n second number')
    try:
        answer=int(first_num)/int(second_num)
    except ZeroDivisionError:
        print('you can not divide by 0!')
    else:
        print(answer)
#FileNotFoundError异常
filename='aice.txt'
try:
    with open(filename) as file_object:
        contents=file_object.read()
except FileNotFoundError:
    msg='sorry the file '+filename+' does not exist'
    print(msg)
else:
    print(contents)
#失败时一声不吭
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        pass #告诉python什么都不做
    else:
        words=contents.split()
        num_words=len(words)
        print('this book has about '+str(num_words)+'words')
#存储数据
import json
numbers=['dantyli','lice','andy','tonny']
filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
with open(filename) as f_obj:
    numbers=json.load(f_obj)
print(numbers)
